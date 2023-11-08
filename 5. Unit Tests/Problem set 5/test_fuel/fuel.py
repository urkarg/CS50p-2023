def main():
    inps = input("Fraction: ")
    fract = convert(inps)
    print(gauge(fract))


def convert(fraction):
    x, y = fraction.split(sep="/")
    z = round(int(x)/int(y)*100, 0)
    if z <= 100:
        return z
    else:
        raise ValueError


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif 99 <= percentage:
        return "F"
    else:
        return f"{percentage:.0f}%"

if __name__ == "__main__":
    main()