def main ():
    camelCase = input("camelCase: ")
    snake_case = from_case_to_underscore(camelCase)
    print(snake_case)


def from_case_to_underscore(word):
    camel_word = ""
    for char in word:
        if char.isupper():
            camel_word += "_" + char.casefold()
        else:
            camel_word += char
    return camel_word


main ()