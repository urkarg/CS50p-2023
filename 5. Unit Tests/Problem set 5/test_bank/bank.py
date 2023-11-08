def main():
    g = input("Greeting: ")
    print(value(g))


def value(greeting):
    g = greeting.strip().casefold()
    if g.startswith("hello"):
        return 0
    elif g.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()