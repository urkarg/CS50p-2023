import inflect

p = inflect.engine()

def main ():
    names = []
    try:
        while True:
            names.append(input("Name: "))
    except EOFError:
        print(f"Adieu, adieu, to {p.join(names)}")


main ()