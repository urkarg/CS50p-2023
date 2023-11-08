import random


def main():
    level = get_level()
    score = 0
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        j = 0
        k = True
        while (j < 3 and k):
            sol = input(f"{x} + {y} = ")
            try:
                if x + y == int(sol):
                    score += 1
                    k = False
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
            j += 1
        if j == 3:
            print(f"{x} + {y} = {x+y}")
    print(f"Score: {score}")


def get_level():
    levels = [1, 2, 3]
    while True:
        try:
            nr = int(input("Level: "))
            if nr in levels:
                return nr
        except ValueError:
            continue


def generate_integer(level):
    if level not in [1, 2, 3]:
        raise ValueError
    if level == 3:
        x = random.randint(100, 999)
    elif level == 2:
        x = random.randint(10, 99)
    else:
        x = random.randint(0, 9)
    return x


if __name__ == "__main__":
    main()