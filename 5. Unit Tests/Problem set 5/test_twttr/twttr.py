def main():
    tweet = input("Input: ")
    twt = shorten(tweet)
    print("Output:", twt)

def shorten(word):
    output_string=""
    vowels_complete =[]
    vowels_lower = ["a","e","i","o","u"]
    vowels_complete += [vowels_upper.upper() for vowels_upper in vowels_lower] + vowels_lower
    for char in word:
        if char in vowels_complete:
            output_string +=""
        else:
            output_string += char
    return output_string.strip()

if __name__ == "__main__":
    main()