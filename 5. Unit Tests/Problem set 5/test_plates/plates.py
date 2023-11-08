def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    has_number = False
    string_length = 0
    for character in s:
        if not character.isalnum():
            return False
        string_length += 1
        if string_length > 6:
            return False
        if character.isnumeric():
            if string_length <= 2:
                return False
            if character == "0" and not has_number:
                return False
            has_number = True
        elif has_number:
            return False
    if string_length < 2:
        return False
    return True

if __name__ == "__main__":
    main()