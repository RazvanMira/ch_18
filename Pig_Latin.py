def main():
    user_input = input("Insert your words: ")
    vowel = ["a", "e", "i", "o", "u"]
    words = user_input.split(" ")
    final_list = []
    for word in words:
        has_upper = False
        has_punctuation = False
        if word[0].isupper():
            has_upper = True
        if not word[-1].isalpha():
            has_punctuation = True
        word = word.lower()
        if has_punctuation:
            punctuation = word[-1]
            word = word[0:-1]
        if word[0] not in vowel:
            index_input = 0
            for index, letter in enumerate(word):
                if letter in vowel:
                    index_input = index
                    break
            result = f'{word[index_input:]}{word[:index_input]}ay'
        else:
            result = f'{word}way'
        if has_punctuation:
            result = result + punctuation
        if has_upper:
            result = result.capitalize()
        final_list.append(result)
    print(" ".join(final_list))

if __name__ == "__main__":
    main()