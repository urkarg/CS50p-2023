import emoji

emj = input("Input: ")
print(f"Output: {emoji.emojize(emj, language='alias')}")