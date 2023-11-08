answer = input("What is the answer to the Great Question of Life, the Univers, and Everything? ")

match answer.casefold().strip():
    case "forty two":
        print("Yes")
    case "42":
        print("Yes")
    case "forty-two":
        print("Yes")
    case _:
        print("No")