import sys
from tabulate import tabulate

table =[]
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif sys.argv[1].endswith(".csv") == False:
    sys.exit("Not a CSV file")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    try:
        with open(sys.argv[1], errors = "FileNotFoundError") as file:
            for line in file:
                pizza_type, price_s, price_l = line.rstrip().split(",")
                row = {}
                row["pizza_type"] = pizza_type
                row["price_s"] = price_s
                row["price_l"] = price_l
                table.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")

print(tabulate(table, headers="firstrow", tablefmt="grid"))