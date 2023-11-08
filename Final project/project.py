import json
import csv
import random
import sys
import re
from tabulate import tabulate
from score_round import ScoreRound
from score_game import ScoreGame

def get_user_choice(kind="roll", output=False, input_func=input):
    """
    Validate the input string of various game moments: during reroll, during score choosing, and during yahtzee score choosing.

    :param kind: can be "roll", "score", "yl" or "y0". Roll validates for a set of rerolls. score valides for a score item. yl and y0 validate for Joker Rules
    :param output: used to create an input loop if the type of input is invalid. output is changed into the input string once input string is valid.
    :type output: bool
    :param input_func: the input function, introduced as a paramater in order to be mocked during unit testing.
    :type input_func: function

    """
    while output==False:
        roll_set = {"1", "2", "3", "4", "5"}
        match kind:
            case "roll":
                input_string:str = input_func(f"If you want to reroll, enter the dice position/s you want to reroll.\nIf not, input (k)eep\n")
                roll = set(input_string)
                if roll.issubset(roll_set) and ("\n") not in roll:
                    output = roll
                elif input_string.lower() == "k":
                    output = input_string
                else:
                    print("Invalid choice")
            case "score":
                input_string = input_func(f"Choose the Item on the score sheet to fill in (a number from 1 to 13), or yahtzee if applicabile:\n")
                if re.search(r"^([1-9]|1[0-3])$", input_string):
                    output = input_string
                else:
                    print("Invalid choice")
            case "yl":
                input_string = input_func(f"Joker rules, applicable. Please choose score Item from Lower Section to fill in:\n")
                if re.search(r"^([7-9]|1[0-3])$", input_string):
                    output = input_string
                else:
                    print("Invalid choice")
            case "y0":
                input_string = input_func(f"Joker rules, applicable. As the Dice pip position and the Lower section are full, select an Item from Upper Section to fill 0 in:\n")
                if re.search(r"^[1-6]$", input_string):
                    output = input_string
                else:
                    print("Invalid choice")

    return output


def load_dice_file(dice_pict_file):
    """
    Open & load the file dices.txt. It will be used to illustrate the dices

    :param dice_pict_file: file containing the dice pictograms
    :return: the contents of the file dices.txt as a dictionary
    :rtype: dict
    """
    try:
        with open(dice_pict_file) as dices_file:
            dices_dict = json.loads(dices_file.read(), strict=False)
        return dices_dict
    except FileNotFoundError:
        sys.exit("Dice file does not exist")


def read_score_csv(csv_file):
    """
    Load and format the score_card.csv file. It will be used to show the score. The csv is read as a dictionary
    A different function is used for writing a game card per game

    :param csv_file: csv containing the score card
    :return: the contents of the score_card.csv, formatted with the tabulate library, grid type
    :rtype: str
    """
    try:
        with open(csv_file) as csv_score_file:
            return tabulate(csv.DictReader(csv_score_file, escapechar="\\"), headers="keys", tablefmt="grid")
    except FileNotFoundError:
        sys.exit("Score file does not exist")


def roll_dice(n=5):
    """
    Creates a list of 5 dice values, as per Yahtzee game

    :param none: the list always has 5 dice values
    :variable i: the value of a dice roll
    :return: a list with the values of the dice rolled
    :rtype: list
    """
    dice_values_list = []
    for i in range(n):
        i = random.randint(1,6)
        dice_values_list.append(i)
    return dice_values_list


def dict_dice_throws(pips_on_throw:list, order=["I", "II", "III", "IV", "V"]):
    """
    Creates a dictionry of dice throws where the key is the ordinal number of the throws, while the value is the nr of pips on the dice

    :param pips_on_throws: List containing the number of pips on each die
    :type pips_on_throws: list
    :param order: a list containing the order of the throws
    :type order: list
    :return: a dictionary with each value linked to the order of the throws
    :rtype: dict
    """
    if len(pips_on_throw) == len(order):
        return {order[i]:pips_on_throw[i] for i in range(len(pips_on_throw))}
    else:
        sys.exit("Initial list of throws is smaller than 5")


def correlate_dice_values(dice_thrown:dict, dice_dict:dict):
    """
    Correlates the value of a dice from the list with the ascii art from the dictionary

    :param dice_thrown: Pips per dice thrown
    :type dice_thrown: dict, the key is the number of dice, the value is the nr of pips per dice
    :param dice_dict: dictionary with pictograms of dice values
    :type dice_dict: dictionary, created with load_dice_file
    :return: a new dictionary where the throw order is populated with the value pictogram from thrown pips
    :rtype: dict
    """
    try:
        return {i:dice_dict[str(dice_thrown[i])] for i in dice_thrown}
    except KeyError:
        sys.exit("Dictionaries in correlate_dice_values can't be compounded")


def dice_to_print(throws_ready:dict):
    """
    Function takes dictionary of dice throws & their values, splits per /n, and prints each line at a time

    :param throws_ready: a dictionary containing order of dice throws and pip value in ascii
    :type throws_ready: dict
    :variable rows: the map function splits each value of a throw per /n and inserts them into a tuple with zip
    :type rows: tuple
    :variable row: element of the tuple created with zip, names rows
    :return: prints a line per execution of loop
    :rtype: None
    """
    for rows in zip(*map(str.splitlines, throws_ready.values())):
        print(*(row for row in rows))


def convert_set_reroll_to_order_list(dice_to_reroll:set):
    """
    Convert the set with dice positions to be rerolled into a list with positions

    :param dice_to_reroll: a set with dice positions to be rerolled
    :type dice_to_reroll: set
    :return: a list with positions which will be rerolled, ranging from I to V
    :rtype: list
    """
    list_of_rerolls = []
    for i in dice_to_reroll:
        match i:
            case "1":
                i = "I"
            case "2":
                i = "II"
            case "3":
                i = "III"
            case "4":
                i = "IV"
            case "5":
                i = "V"
            case _:
                sys.exit("Position reroll in convert_set_to_order_list is not a number from 1 to 5")
        list_of_rerolls.append(i)
    return list_of_rerolls


def main():
    try:
        print("""
Yahtzee is a dice game based on Poker.
The objective of the game is to score points by rolling five dice to make certain combinations.
The dice can be rolled up to three times in a round. The game has 13 rounds
After you finish rolling, you must place a score or a zero in one of the 13 category boxes on your score card.""")
        game_round = 1
        pips_ascii = load_dice_file("dices.txt")
        game_score = ScoreGame()
        score = ScoreRound()
        #Each game rounds uses the same class instances
        while game_round<=13:
            #ybc stands for yahtzee bonus count. It becomes true if the bonus was counted during that round
            ybc=False
            #gsd stands for game score dictionary, used to accumulate user's score choices
            gsd:dict = game_score.game_score_dict_build()
            game_score.convert_db_to_csv()
            print(read_score_csv("db_score_card.csv"))
            dice_values = roll_dice()
            dice_values.sort()
            pips_per_dice = dict_dice_throws(dice_values)
            dice_values_with_ascii = correlate_dice_values(pips_per_dice, pips_ascii)
            dice_to_print(dice_values_with_ascii)
            print(f"Round {game_round}")
            #this if ensures that if a yahtzee was rolled (the second 5 in a row. not possible in the first round)
            #the yahtzee score table is shown, according to joker rules
            #script repeats during reroll phase
            if game_round != 1 and score.yahtzee_check(gsd) =="Yahtzee!":
                score.build_score(pips_per_dice, gsd, y=True)
            else:
                score.build_score(pips_per_dice, gsd)
            print(f"Initial score: {score}\n")
            rerolls=0
            while(rerolls<2):
                """
                The reroll sequence can happen two times.
                Dice values will be saved in the variable dice_values, by overwriting previous values, if rerolling.
                pips_per_dice will be updated with the reroll values, and will be used for score calculations
                dice_values_with_ascii will also be overwritten
                """
                rerolls_set = get_user_choice("roll")
                if rerolls_set == "k":
                    break
                else:
                    rerolls_positions = convert_set_reroll_to_order_list(rerolls_set)
                    dice_values = roll_dice(len(rerolls_positions))
                    pips_per_dice2 = dict_dice_throws(dice_values, rerolls_positions)
                    pips_per_dice.update(pips_per_dice2)
                    dice_values_with_ascii = correlate_dice_values(pips_per_dice, pips_ascii)
                    dice_to_print(dice_values_with_ascii)
                    rerolls +=1
                    if game_round != 1 and score.yahtzee_check(gsd) =="Yahtzee!":
                        score.build_score(pips_per_dice, gsd, y=True)
                    else:
                        score.build_score(pips_per_dice, gsd)
                    print(f"Reroll {rerolls} score:{score}")
            #The role of this loop is to ensure that the score item was not already filled in, and to factor in the Joker Rules
            while True:
                #Yahtzee check starts here
                if score.yahtzee =="Yahtzee!":
                    #if a Yahtzee has already been filled in, Joker Rules apply from here on
                    if gsd["12"] == 50 and ybc == False:
                        #Upper score section with Yahtzee type is free, it's going to be filled in automatically
                        if str(score.yahtzee_type) not in gsd.keys():
                            print("Joker Rules applicable! Score the total of all five dice in the Upper section!")
                            score_item = str(score.yahtzee_type)
                        #Upper score section and all of lower section filled in, a 0 will be inputted in the free upper section slot
                        elif sum([int(i) for i in gsd.keys()]) >= 70:
                            score_item = get_user_choice(kind ="y0")
                        #Upper score section filled in, Joker Rules apply and item in lower section will be filled in
                        else:
                            score_item = get_user_choice(kind="yl")
                        game_score.yahtzee_bonus()
                        ybc=True
                else:
                    #No Yahtzee, standard score choice
                    score_item = get_user_choice(kind="score")
                if score_item not in gsd.keys():
                    round_save = score.choose_score_entry(score_item)
                    break
                else:
                    print("Score item already filled in!")
            print(f"End of game round {(game_round)}")
            game_score.fill_in_roundscore(score_item, round_save)
            game_round += 1
        game_score.end_game()
        game_score.convert_db_to_csv()
        print(read_score_csv("db_score_card.csv"),"\nThank you for playing!")
        game_score.flush_score()
    #used mostly for testing, but it's a very useful feature
    except KeyboardInterrupt:
        game_score.flush_score()


if __name__ == "__main__":
    main()
