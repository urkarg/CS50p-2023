import sqlite3
import sys
import pandas as pd

class ScoreGame():

    def __init__(self, idb="score_card.db", table="score"):
        """
        Initiating the common variables in the class. Optional paramaters hard-coded with the database and the table that my program uses.

        :param idb: string containing the database to which we're connecting with sqlite
        :type idb: str
        :param table: string containing the table inside the database. In this case, it's names "score"
        :type table: str

        Other initialized values:
        db = connection to the database idb
        arrow = creating a cursor for the database
        game_score_dict_up = the dictionary containing the scores of the upper section
        game_score_dict_low = the dictionary containing the scores of the lower section
        game_score_dict = the dictionary containing the scores the whole game, created with the game_score_dict_build
        yb = yahtzee bonus count
        ubv = upper bonus value, will be equal with 35, happens only once at the end of the game
        up = the sum of the game_score_dict_up values
        low = the sum of the game_score_dict_low values

        """
        self.db = sqlite3.connect(idb)
        self.arrow = self.db.cursor()
        self.game_score_dict_up = {}
        self.game_score_dict_low = {}
        self.game_score_dict = {}
        self.yb = 0
        self.ubv = 0
        self.table = table
        self.up = 0
        self.low = 0

    def game_score_dict_build(self):
        """ Creates the game score dictionary - gsd """
        self.game_score_dict.update(self.game_score_dict_low)
        self.game_score_dict.update(self.game_score_dict_up)
        return self.game_score_dict

    def flush_score(self):
        """ Fills in the Score column with blanks, so that one can start a new game """
        for i in range(25):
            self.arrow.execute(f"""UPDATE {self.table} SET Score = " " WHERE rowid = "{i}";""")
        self.db.commit()
        print("\nFlush complete")

    def fill_in_roundscore(self, item, round_score:dict):
        """
        Takes in the score of the round, sorts it into upper and lower section, creates subtotals for the 2 sections, and commits everything into the data base

        :param item: a number to indicate which score item will be filled it
        :type item: str; to be converted in int
        :param round_score: a dictionary with the key equal to item, and the value equal to the score to be inputted in the database
        :type round_score: dict

        """
        if round_score != {}:
            if 1 <= int(item) <= 6:
                self.game_score_dict_up[item] = round_score[item]
                self.arrow.execute(f"""UPDATE {self.table} SET Score = {round_score[item]} WHERE Item = "{item}";""")
            else:
                self.game_score_dict_low[item] = round_score[item]
                self.arrow.execute(f"""UPDATE {self.table} SET Score = {round_score[item]} WHERE Item = "{item}";""")
            self.up = sum(self.game_score_dict_up.values(), self.ubv)
            self.low = sum(self.game_score_dict_low.values())
            self.arrow.execute(f"""UPDATE {self.table} SET Score = {self.up} WHERE RowNr = 7;""")
            self.arrow.execute(f"""UPDATE {self.table} SET Score = {self.low} WHERE RowNr = 20;""")
            self.arrow.execute(f"""UPDATE {self.table} SET Score = {self.up+self.low} WHERE RowNr = 22;""")
            self.db.commit()

    def yahtzee_bonus(self):
        """ Calculates and increments the yahtzee bonus, but it doesn't calculate the score yet """
        self.arrow.execute(f"""UPDATE {self.table} SET Score = "Check x {self.yb}" WHERE RowNr = 19;""")
        self.yb +=1

    def end_game(self):
        """ Calculates and updates the upper bonus, if applicable, and adds the score from the yahtzee bonuses """
        if self.up >= 63:
            self.ubv=35
            self.arrow.execute(f"""UPDATE {self.table} SET Score = {self.ubv} WHERE RowNr = 8;""")
            self.arrow.execute(f"""UPDATE {self.table} SET Score = {self.up+self.ubv} WHERE RowNr = 9;""")
        else:
            self.arrow.execute(f"""UPDATE {self.table} SET Score = {self.up} WHERE RowNr = 9;""")
        self.arrow.execute(f"""UPDATE {self.table} SET Score = {self.up+self.low+(100*self.yb)} WHERE RowNr = 22;""")
        self.db.commit()

    def convert_db_to_csv(self):
        """
        Transform a db_file into a csv using Panda and sqlite3. Exits with Sys if the score file doesn't exist

        :param db_file: database file containing the score card
        :return: the database as a csv file db_score_card.csv. Will be sent to formatting in the function read_score_csv
        :rtype: csv
        """
        try:
            df = pd.read_sql_query("""select Item,Section,"What to Score",Score from score""", self.db)
            df.to_csv("db_score_card.csv", index=False)
        except FileNotFoundError:
            sys.exit("Score file does not exist")
