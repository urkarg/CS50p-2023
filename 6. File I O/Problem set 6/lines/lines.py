import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif sys.argv[1].endswith(".py") == False:
    sys.exit("Not a Python file")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    try:
        with open(sys.argv[1], "r", errors = "FileNotFoundError") as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")

count = 0
for line in lines:
    line = line.lstrip()
    if line:
        if line.startswith("#") == False:
            count += 1

print(count)