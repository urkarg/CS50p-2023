def main():
    z = percent()
    if z <= 0.01:
        print("E")
    elif 1 >= z >= 0.99:
        print("F")
    else:
        print(f"{(z)*100:.0f}%")


def percent ():
    while True:
        try:
            x, y = input("Fraction: ").split(sep="/")
            z = int(x)/int(y)
            if z <= 1:
                return z
        except (ValueError, ZeroDivisionError):
            pass


main()