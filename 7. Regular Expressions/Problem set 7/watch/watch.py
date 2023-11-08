import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if ys := re.search(r'^<iframe.*src="(https?://)?(www\.)?youtube\.com/embed/(.*?)".*></iframe>$', s):
        return f"https://youtu.be/{ys.group(3)}"
    else:
        return None


if __name__ == "__main__":
    main()