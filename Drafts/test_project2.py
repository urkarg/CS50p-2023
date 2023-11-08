import pytest
import project
import unittest
import mock
from score_game import ScoreGame
from score_round import ScoreRound

pip_dict_y6 = {"I":6, "II":6, "III":6, "IV":6, "V":6}
pip_dict_y5 = {"I":5, "II":5, "III":5, "IV":5, "V":5}

def pip_dict_y(i):
    return {"I":i, "II":i, "III":i, "IV":i, "V":i}

def pip_list_y(i):
    return [i, i, i, i, i]


def game_rounds(game_round, game_score:ScoreGame, score:ScoreRound, pips_ascii):
    while game_round<=13:
        ybc=False
        gsd:dict = game_score.game_score_dict()
        game_score.convert_db_to_csv()
        print(project.read_score_csv("db_test_score_card.csv"))
        dice_values = pip_list_y(1)
        dice_values.sort()
        pips_per_dice = project.dict_dice_throws(dice_values)
        dice_values_with_ascii = project.correlate_dice_values(pips_per_dice, pips_ascii)
        project.dice_to_print(dice_values_with_ascii)
        print(f"Round {game_round}")
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
            rerolls_set = project.get_user_choice("roll")
            if rerolls_set == "Keep":
                break
            else:
                rerolls_positions = project.convert_set_reroll_to_order_list(rerolls_set)
                dice_values = project.roll_dice(len(rerolls_positions))
                pips_per_dice2 = project.dict_dice_throws(dice_values, rerolls_positions)
                pips_per_dice.update(pips_per_dice2)
                dice_values_with_ascii = project.correlate_dice_values(pips_per_dice, pips_ascii)
                project.dice_to_print(dice_values_with_ascii)
                rerolls +=1
                if game_round != 1 and score.yahtzee_check(gsd) =="Yahtzee!":
                    score.build_score(pips_per_dice, gsd, y=True)
                else:
                    score.build_score(pips_per_dice, gsd)
                print(f"Reroll {rerolls} score:{score}")
        while True:
            if score.yahtzee =="Yahtzee!":
                score_item = project.get_user_choice(kind="yahtzee")
                if gsd["12"] == 50 and ybc == False:
                    game_score.yahtzee_bonus()
                    ybc=True
            else:
                score_item = project.get_user_choice(kind="score")
            if score_item not in gsd.keys():
                round_save = score.choose_score_entry(score_item)
                break
            else:
                print("Score item already filled in!")
        print(f"End of game round {(game_round)}")
        game_score.fill_in_roundscore(score_item, round_save)
        game_round += 1

def main():
    try:
        test_game_round = 1
        pips_ascii = project.load_dice_file("dices.txt")
        test_game_score = ScoreGame(table="test_score")
        test_score = ScoreRound()
        game_rounds(test_game_round, test_game_score, test_score, pips_ascii)
    except KeyboardInterrupt:
        test_game_score.flush_score()

main()
