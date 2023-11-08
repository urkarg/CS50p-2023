import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    return len(re.findall(r"\bum(\W|\b)", s.casefold()))


if __name__ == "__main__":
    main()