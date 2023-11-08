import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif sys.argv[1].endswith(".csv") == False:
    sys.exit("Not a CSV file")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    try:
        with open(sys.argv[2], "w") as scorg:
            scorg = csv.DictWriter(scorg, fieldnames=["first","last","house"])
            scorg.writeheader()
        with open(sys.argv[1], errors = "FileNotFoundError") as before:
            list = csv.DictReader(before)
            for line in list:
                house = line["house"]
                last, first = line["name"].split(", ")
                with open(sys.argv[2], "a") as scorg:
                    scorg = csv.DictWriter(scorg, fieldnames=["first","last","house"])
                    scorg.writerow({"first": first, "last": last, "house": house})
    except FileNotFoundError:
        sys.exit("File does not exist")