# Happy path! All letters have the same case

## The case with all lower case

list_to_sort = [
    "david",
    "bob",
    "carol",
    "alice",
    "emily"
]

list_to_sort.sort()
print("lowercase: ", list_to_sort)

## The case with all upper case - the same


# Not the happy path! The letters have different cases

list_to_sort = [
    "david",
    "Bob",
    "carol",
    "Alice",
    "emily"
]

list_to_sort.sort(key=str.casefold)
print("mixed case: ", list_to_sort)


# How will the words be sorted?

list_to_sort = [
    "david",
    "Bob",
    "carol",
    "Alice",
    "emily",
    "Franklin",
    "george"
]

list_to_sort.sort(key=len)
print("surprise sort: ", list_to_sort)


# How will the words be sorted?

def starts_with_vowel(string: str) -> int:
    if string[0].casefold() in "aeiou":
        return 1
    else:
        return 0

list_to_sort = [
    "david",
    "Bob",
    "carol",
    "Alice",
    "emily",
    "Franklin",
    "george"
]

list_to_sort.sort(key=starts_with_vowel)
print("second surprise sort: ", list_to_sort)


# How will the words be sorted?

def extract_second_letter(word: str) -> str:
    second_letter = word[1]
    return second_letter

list_to_sort = [
    "david",
    "Bob",
    "carol",
    "Alice",
    "emily",
    "Franklin",
    "george"
]

list_to_sort.sort(key=extract_second_letter)
print("last surprise sort: ", list_to_sort)