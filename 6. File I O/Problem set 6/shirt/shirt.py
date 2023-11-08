import sys
from PIL import Image
from PIL import ImageOps

ext = [".png",".jpg",".jpeg"]

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        for j in [1,2]:
            if sys.argv[j].casefold().endswith(tuple(ext)) == False:
                sys.exit("Invalid input")
        if(sys.argv[1].split(".")[1] != sys.argv[2].split(".")[1]):
            sys.exit("Input and output have different extensions")

    try:
        try_shirt()
    except FileNotFoundError:
        sys.exit("File does not exist")

def try_shirt():
    shirt = Image.open("shirt.png")
    meep = Image.open(sys.argv[1])
    shirt_size = shirt.size
    shirt_meep = ImageOps.fit(meep, size=shirt_size)
    shirt_meep.paste(shirt, shirt)
    shirt_meep.save(sys.argv[2])

main()