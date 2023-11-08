import sys
import random

from pyfiglet import Figlet
figlet = Figlet()
list_of_fonts = figlet.getFonts()

if len(sys.argv) == 1:
    s = input("Input: ")
    figlet.setFont(font = random.choice(list_of_fonts))
    print(f"Output:\n {figlet.renderText(s)}")
elif len(sys.argv) == 3:
    if sys.argv[1] == ("-f" or "--font"):
        s = input("Input: ")
        figlet.setFont(font=sys.argv[2])
    else:
        sys.exit("Invalid usage")
    print(f"Output\n: {figlet.renderText(s)}")
else:
    sys.exit("Invalid usage")