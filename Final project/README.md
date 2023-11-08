# Yahtzee - in python
#### Video Demo: https://youtu.be/svbCFLLLu9g
#### Description:

Yahtzee - in python is an implementation of the dice game Yahtzee in Python.
This project was an undertaking that i was sure i could finish, but I was also sure I wouldn't be able to test automatically, due to the high complexity of the main function, and due to my lack of unit testing knowledge. I feel that i could've invested more time to properly create a suite of testing for the 2 class files that I've used.
Either way, I am proud of what I've done, and I really hope that someone will look over my code and say that - hey, this rookie did a pretty swell job. Now then, onto the documentation.

## Part I - Project.py, main function, additional functions
The project was built incrementally, and I've constantly looked for design improvements, by rubber duck debugging, and by asking the help of various people that i work with and that I have around me. I simply couldn't abstain from showing them my work, and promprting improvement ideas either from them, either from my talking to them.
The project simulates a complete game of Yahtzee, single player, with a score sheet and dice pictograms. The game has 13 rounds, after all the rounds have been played, the final score is tallied and showed one last time on the screen. The programs runs inside a terminal, so it has a lot of repetitive printing. Someday, I might learn to implement a front end for it.
### The project files:
- project.py - here is the bulk of the code. It contains some additional functions that could be tested from the outside of the file, and the main function which uses everything else to illustrate and play the game
- dices.txt - text file with pictograms for dice. Imported inside project.py with the help of json library
- score_game.py - contains the class ScoreGame, used for interacting with the database, and for storing the game score. One instance created at the start of the game
- score_round.py - contains the class ScoreRound, used for calculating the individual round scores, for printing them inside main, and for selecting one entry and sending it to ScoreGame
- score_card.db - contains the database where the table named "score" (lower case s) holds the game score
- db_score_card.csv - csv export from the database, used for creating the nifty table on top of every score round. Created with tabulate. I really like tabulate.
- test_project.py - file contains unit tests for the custom functions used in the generation of the game items

### Short history
The project has gone through various refactorings, as I've notice that i simply can't do what I want with the current architecture.
Initially, I had a class called Scoring, that was supposed to handle everything related to scoring, so it was used to calculate the score, printing it, sending it in the database, exporting it for csv etc.
Then, I noticed that it was too large, and I split it in two, one for scoring a round, one for scoring the game. Then, I received an outsite tip (thank you Madalin), that the convention is that classes are held in separate files, so i took them apart, and started remapping the classes and their methods.
And here I was, with plenty of tests written for the initial Scoring class, due to my proactivity, that had to be completely thrown away, and restarted. Frankly, I would've made a third class with the rest of the custom functions, but in the end, this is something that can be improved after the course.

### Libraries used
- json: for importing and reading the dice file
- csv: for handling the csv created by pandas
- random: for rolling the dice
- sys: for exiting during a file input error
- re: for validation the user's actions when rerolling or scoring
- tabulate: for pretty printing
- sqlite3: for handling the database
- pandas: for the database export in csv
- pytest: for unit testing
- collections: for the counter functions, used for x of a kind calculations

### How does it work?
I'll go through the main function using the comments I've inputted in the code, and some more addendums here and there:
```ruby
try: #---> program starts with a try except KeyboardInterrupt that clear the database Score column. Very useful for manual testing. A lot of manual testing was done.
        print("""
Yahtzee is a dice game based on Poker.
The objective of the game is to score points by rolling five dice to make certain combinations.
The dice can be rolled up to three times in a round. The game has 13 rounds
After you finish rolling, you must place a score or a zero in one of the 13 category boxes on your score card.""") #---> printed a short intro to the rules of Yahtzee. Feedback from friends that had no idea what was happening here.
        game_round = 1 #---> game starts at round 1
        pips_ascii = load_dice_file("dices.txt") #---> load_dice_file loads in the dice pictograms from dices.txt
        game_score = ScoreGame() #---> class instance for the game score
        score = ScoreRound() #---> class instance for round score
        #Each game rounds uses the same class instances
        while game_round<=13: #---> game runs for 13 rounds, then while stops, and program calculates the score
            #ybc stands for yahtzee bonus count. It becomes true if the bonus was counted during that round
            ybc=False
            #gsd stands for game score dictionary, used to accumulate user's score choices
            gsd:dict = game_score.game_score_dict_build()
            game_score.convert_db_to_csv() #---> data from database is exported and converted in CSV
            print(read_score_csv("db_score_card.csv")) #---> CSV is printed prettily with tabulate
            dice_values = roll_dice() #---> 5 dice are rolled by default, to start a yahtzee game
            dice_values.sort()
            pips_per_dice = dict_dice_throws(dice_values) #---> a dictionary of throws is generated, with the order of the throws, such as {I:1, II:2 etc}
            dice_values_with_ascii = correlate_dice_values(pips_per_dice, pips_ascii) #---> order of throw is associated with pictogram of dice pip, where the pip illustration is the value in the dict
            dice_to_print(dice_values_with_ascii) #---> print the pips with a convoluted print function that shows the dice one next to another
            print(f"Round {game_round}") #--->
            #this if ensures that if a yahtzee was rolled (the second 5 in a row. not possible in the first round)
            #the yahtzee score table is shown, according to joker rules
            #script repeats during reroll phase
            if game_round != 1 and score.yahtzee_check(gsd) =="Yahtzee!": #---> Yahtzee checks that help with the special yahtzee scoring below
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
                rerolls_set = get_user_choice("roll") #---> user selects with dice to reroll by typing a number from 1 to 5, or by typing k if he wants to keep them
                if rerolls_set == "k":
                    break
                else: #---> this section contains a very similar sequence to the one above, that is particular to the dice rerolls
                    rerolls_positions = convert_set_reroll_to_order_list(rerolls_set)
                    dice_values = roll_dice(len(rerolls_positions))
                    pips_per_dice2 = dict_dice_throws(dice_values, rerolls_positions)
                    pips_per_dice.update(pips_per_dice2) #---> initial dict with dice pips is updated, as the keys are identical, and sent for correlation with pictograms and printing
                    dice_values_with_ascii = correlate_dice_values(pips_per_dice, pips_ascii)
                    dice_to_print(dice_values_with_ascii)
                    rerolls +=1
                    if game_round != 1 and score.yahtzee_check(gsd) =="Yahtzee!":
                        score.build_score(pips_per_dice, gsd, y=True)
                    else:
                        score.build_score(pips_per_dice, gsd)
                    print(f"Reroll {rerolls} score:{score}")
            #The role of this loop is to ensure that the score item was not already filled in, and to factor in the Joker Rules
            while True: #---> details on how to calculate yahtzee bonuses and joker rules. This was initially in the score_game file, more or less hard-coded in the database, but then I took it out and considered it is more fitting to have it in the main function, using the score instance of ScoreRound class for the yahtzee value and for the special values of the Joker Rules
                #Yahtzee check starts here
                if score.yahtzee =="Yahtzee!":
                    #if a Yahtzee has already been filled in, Joker Rules apply from here on
                    if gsd["12"] == 50 and ybc == False:
                        #Upper score section with Yahtzee type is free, it's going to be filled in automatically
                        if str(score.yahtzee_type) not in gsd.keys():
                            print("Joker Rules applicable! Score the total of all five dice in the Upper section!")
                            score_item = str(score.yahtzee_type)
                        #Upper score section and all of lower section filled in, a 0 will be inputted in the free upper section slot
                        elif sum([int(i) for i in gsd.keys()]) >= 70: #---> mathy way to check if all the lower section keys have been filled in, and ensure that the program doesn't loop
                            score_item = get_user_choice(kind ="y0")
                        #Upper score section filled in, Joker Rules apply and item in lower section will be filled in
                        else:
                            score_item = get_user_choice(kind="yl")
                        game_score.yahtzee_bonus()
                        ybc=True
                else:
                    #No Yahtzee, standard score choice
                    score_item = get_user_choice(kind="score")
                if score_item not in gsd.keys(): #---> validation of user input, to see if the score category hasn't already been filled in
                    round_save = score.choose_score_entry(score_item)
                    break
                else:
                    print("Score item already filled in!")
            print(f"End of game round {(game_round)}")
            game_score.fill_in_roundscore(score_item, round_save) #---> the game score class is updated with the round's score and choices, and gsd is updated
            game_round += 1 #---> a new round starts
        game_score.end_game() #---> bonus for additional yahtzee and for reaching the upper section bonus are calculated
        game_score.convert_db_to_csv() #---> one last conversion
        print(read_score_csv("db_score_card.csv"),"\nThank you for playing!") #---> one last score card printing
        game_score.flush_score() #---> database is flushed clear of the score
    #used mostly for testing, but it's a very useful feature
    except KeyboardInterrupt:
        game_score.flush_score()
```

### Custom functions:
They are thoroughly documented in the code, I am going to list them here:

- get_user_choice: Validate the input string of various game moments: during reroll, during score choosing, and during yahtzee score choosing.
- load_dice_file: Open & load the file dices.txt. It will be used to illustrate the dices
- read_score_csv: Load and format the score_card.csv file. It will be used to show the score. The csv is read as a dictionary. A different function is used for writing a game card per game
- roll_dice: Creates a list of 5 dice values, as per Yahtzee game
- dict_dice_throws: Creates a dictionry of dice throws where the key is the ordinal number of the throws, while the value is the nr of pips on the dice
- correlate_dice_values: Correlates the value of a dice from the list with the ascii art from the dictionary
- dice_to_print: Function takes dictionary of dice throws & their values, splits per /n, and prints each line at a time
- convert_set_reroll_to_order_list: Convert the set with dice positions to be rerolled into a list with positions

## Part 2 - the Score classes
The program contains two score classes, one for the game, one for the round

### score_game class
The ScoreGame class contains the database handling and the database conversion operations. It increments and holds in the score of the game, while sending it and retrieving it from the db.
The structure is at follows:
- __init__ - initialiazes the database, the game score dictionaries and the game score upper and lower section sums
- game_score_dict_build: Creates the game score dictionary - gsd
- flush_score: Fills in the Score column with blanks, so that one can start a new game
- fill_in_roundscore: Takes in the score of the round, sorts it into upper and lower section, creates subtotals for the 2 sections, and commits everything into the data base. This is the most important function of the class, as it takes in the round score selected by the user, and sends it towards the database
- yahtzee_bonus: Calculates and updates the upper bonus, if applicable, and adds the score from the yahtzee bonuses
- convert_db_to_csv: Transform a db_file into a csv using Panda and sqlite3. Exits with Sys if the score file doesn't exist.

### score_round class
The ScoreRound class contains all the score calculations per round, and feeds some of its data to the ScoreGame class. It didn't require an initialization, as I could peep in and take some values for certain checks in the main without it.
The structure is as follows:
- yahtzee_check: Method checks if the roll is yahtzee, and return the yahtzee answer, calculated with the (low_total_dice function, kind="y") method
- build_score: Build score method takes in 2 dictionaries and is also used to show the joker rules in case of a yahtzee. This is the bulk of the class, where all the scores are calculated.
- _up_score: Instance method to calculate sum of pips on throws, used for all upper section scores
- _low_total_dice: Instance method that calculates the score for three of a kind, four of a kind, five of a kind(yahtzee) and full house. Contains additional data if one rolls a yahtzee, such as a yahtzee type, used in the main function
- _straight: Instance method that return the scores of the 2 types of straight, small and large.
- get_score_map: Creates the round score dictionary, from where a score will be selected to be written in the game score dictionary
- choose_score_entry: Method to split the round score that will be written in the game score. Selects only 1 item from the round score dictionary created by get_score_map
- __str__: prints the scores from both upper and lower section, so that the user can select which one he wants to keep

## Unit testing & manual testing
Most of the testing was done manually by playing an replaying the game until the rules worked as expeted. It was especially difficult to test the multiple yahtzee scenarion. In the end, I just inputted a dummy dictionary with a yahtzee instead of the rolled dice, and went through multiple tests to see how the Yahtzee rules and the Joker Rules behave.
The unit tests cover most of the custom functions, with the exception of the printing ones, that were tested manually exhaustively.

## Final words
This project was made with dedication and love, and I had loads of fun working on and applying everything I learned during CS50. Thank you for this opportunity, all the best from me and from Romania, looking forward to the next course!

# Thank you!
