def main():
    string = input("Any emoticons will evolve into emojis\n")
    convert(string)

def convert (slower):
    slower = slower.replace(":)", "🙂")
    slower = slower.replace(":(", "🙁")
    print(slower)

main()