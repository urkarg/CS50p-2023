import sqlite3
import re
import pandas as pd

j ={
 1:"Total of Aces only",
 2:"Total of Twos only",
 3:"Total of Threes only",
 4:"Total of Fours only",
 5:"Total of Fives only",
 6:"Total of Sixes only",
 7:"---->",
 8:"if Total Score >= 63, Score 3",
 9:"---->",
10:"",
11:"",
12:"Add Total of All Dice",
13:"Add Total of All Dice",
14:"Score 25",
15:"Score 30",
16:"Score 40",
17:"Score 50",
18:"Score Total of All Dice",
19:"Score 100 for each bonus chip",
20:"---->",
21:"",
22:"====>"}

con = sqlite3.connect("score_card.db")
cur = con.cursor()
cur.execute("""CREATE TABLE test_score AS SELECT * FROM score; """)
#cur.execute(f"""UPDATE score SET RowNr = {zero} WHERE "What to Score" = "---->";""")
#for i in j:
#    cur.execute(f"""update score set "What to Score" = "{j[i]}" where RowNr = {i}""")
#con.commit()
df = pd.read_sql_query("select * from test_score", con)
df.to_csv("db_test_score_card.csv", index=True)

#db = sqlite3.connect("score_card.db")
#arrow = db.cursor()
#db.commit()
#df = pd.read_sql_query("select * from score", db)
#df.to_csv("db_score_card.csv", index=True)
