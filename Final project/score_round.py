from collections import Counter

class ScoreRound:

    def yahtzee_check(self, gsd={}):
        """ Method checks if the roll is yahtzee, and return the yahtzee answer, calculated with the low_total_dice, kind y method"""
        return self._low_total_dice(gsd, kind="y")

    def build_score(self, pip_dict:dict={}, gsd={}, y=False):
        """
        Build score method takes in 2 dictionaries and is also used to show the joker rules in case of a yahtzee.
        :param pip_dict: dictionary containing the round score
        :type pip_dict: dict
        :param gsd: dictionary containing the game score, build in the ScoreGame class
        :type gsd: dict
        :param y: yahtzee check, used to show the joker rules, when printing
        :type y: boolean

        up_score function builds the scores in the upper section
        y == true show the joker rules scores
        straight function checks if there's a straight
        low_total_dice calculates the score for the rest of the lower section, not covered by straight
        get_score_map created the dictionary for the round score, used to select a score.
        yahtzee_type separately stores the pip value of the yahtzee
        """
        self.pip_dict:dict = pip_dict
        self.ones = self._up_score(1)
        self.twos = self._up_score(2)
        self.threes = self._up_score(3)
        self.fours = self._up_score(4)
        self.fives = self._up_score(5)
        self.sixes = self._up_score(6)
        if y == True:
            self.fullhouse = 25
            self.sstraight = 30
            self.lstraight = 40
        else:
            self.sstraight = self._straight(type="s")
            self.lstraight = self._straight(type="l")
            self.fullhouse = self._low_total_dice(kind="full")
        self.threekind = self._low_total_dice(kind="t")
        self.fourkind = self._low_total_dice(kind="f")
        self.yahtzee = self.yahtzee_check(gsd)
        self.chance = self._low_total_dice(kind="c")
        self.score_dict = self.get_score_map()

    def _up_score(self, pip_int:int, pip_score=0):
        """
        Instance method to calculate sum of pips on throws, used for all upper section scores

        :param pip_int: which die pip is being calculated
        :type pip_int: int
        :param pip_score: variable where the score of the pip sum will be saved
        :type pip_score: int
        :return: sum of pips of the same type on dice
        :rtype: int

        pip_dict contains the values of the rolls for the round.
        """
        for i in self.pip_dict.values():
            if i == pip_int:
                pip_score += pip_int
        return pip_score

    def _low_total_dice(self, gsd:dict={}, kind="c"):
        """
        Instance method that calculates the score for three of a kind, four of a kind, five of a kind(yahtzee) and full house
        Three of a kind: 3 dice with the same number of pips, score is calculated by summing the total value of dice
        Four of a kind: 4 dice with the same number of pips, score is calculated by summing the total value of dice
        Fife of a kind(Yahtzee): score is 50
        Full house: 3 dice of a kind + a different pair of dice, score is 25
        Chance: score is calculated by summing the total value of dice

        :param gsd: dictionary containing the game score. Checks if there has been a 5 of a kind in the game.
        :type gsd: dict
        :param kind: optional, can have 5 values:
            "c" for calculating chance (default value)
            "t" for calculating three of a kind,
            "f" for calculating four of a kind,
            "y" for calculating five of a kind/yahtzee
            "full" for calculating full house
        :type kind: str
        :return: score depending on param kind, and Yahtzee if there has already been a five of a kind the game
        :rtype: int and str, if Yahtzee!
        """
        count_kind = Counter(self.pip_dict.values())
        match kind:
            case "c":
                return sum(self.pip_dict.values())
            case "t":
                for i in count_kind.values():
                    if i >= 3:
                        return sum(self.pip_dict.values())
                return 0
            case "f":
                for i in count_kind.values():
                    if i >= 4:
                        return sum(self.pip_dict.values())
                return 0
            case "y":
                for i in count_kind.values():
                    if i == 5:
                        self.yahtzee_type = self.pip_dict["I"]
                        if "12" in gsd.keys():
                            return "Yahtzee!"
                        else:
                            return 50
                return 0
            case "full":
                if len(count_kind.values()) == 2:
                    for (i,j) in (count_kind.values(), count_kind.values()):
                        if (i,j) == (3,2) or (i,j) == (2,3):
                            return 25
                else:
                    return 0

    def _straight(self, type="s"):
        """
        Instance method that return the scores of the 2 types of straight, small and large.
        A small straight is an ascending sequence of 4 dice, 3 possible sequences (1,2,3,4; 2,3,4,5; 3,4,5,6)
        A large straight is an ascending sequence of 5 dice, 2 possible sequences (1,2,3,4,5; 2,3,4,5,6)

        :param self.pip_dict: dictionary with key: order of throw and value: pips on throw
        :type pip_dict: dict
        :param type: "s" for small straight and "l" for large straight; default to "s"
        :type type: str, optional
        :return: score value of small straight (30) or large straigt (40)
        :rtype: int
        """
        smalls = [[1,2,3,4], [2,3,4,5], [3,4,5,6]]
        larges = [[1,2,3,4,5], [2,3,4,5,6]]
        if type == "s":
            for i in smalls:
                if set(i).issubset(set(self.pip_dict.values())):
                    return 30
            return 0
        if type == "l":
            for i in larges:
                if set(i).issubset(set(self.pip_dict.values())):
                    return 40
            return 0

    def get_score_map(self):
        """ Creates the round score dictionary, from where a score will be selected to be written in the game score dictionary"""
        return {
    "1":self.ones,
    "2":self.twos,
    "3":self.threes,
    "4":self.fours,
    "5":self.fives,
    "6":self.sixes,
    "7":self.threekind,
    "8":self.fourkind,
    "9":self.fullhouse,
    "10":self.sstraight,
    "11":self.lstraight,
    "12":self.yahtzee,
    "13":self.chance
        }

    def choose_score_entry(self, score_to_save):
        """ Method to split the round score that will be written in the game score

        :param score_to_save: the key of the dict entry that will be used to save the score
        :type score to save: int

        uses get_score_map to create the score_dict
        """
        return {score_to_save:self.score_dict[score_to_save]}

    def __str__(self):
        return f"""
    Upper Section:
    1. Ones: {self.score_dict["1"]}
    2. Twos: {self.score_dict["2"]}
    3. Threes: {self.score_dict["3"]}
    4. Fours: {self.score_dict["4"]}
    5. Fives: {self.score_dict["5"]}
    6. Sixes: {self.score_dict["6"]}

    Lower Section
    7. Three of a kind = {self.score_dict["7"]}
    8. Four of a kind = {self.score_dict["8"]}
    9. Full House = {self.score_dict["9"]}
    10. Small straight = {self.score_dict["10"]}
    11. Large straight = {self.score_dict["11"]}
    12. Yahtzee  = {self.score_dict["12"]}
    13. Chance = {self.score_dict["13"]}
        """
