def main():
    tweet = input("Input: ")
    twt = voweliminate(tweet)
    print("Output:", twt)

def voweliminate(input_string):
    output_string=""
    vowels_complete =[]
    vowels_lower = ["a","e","i","o","u"]
    vowels_complete += [vowels_upper.upper() for vowels_upper in vowels_lower] + vowels_lower
    for char in input_string:
        if char in vowels_complete:
            output_string +=""
        else:
            output_string += char
    return output_string

main()