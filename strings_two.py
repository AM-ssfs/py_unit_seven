def four_letters(phrase):
    abc = phrase.split(" ")
    for x in range(len(abc)):
        if len(abc[x]) == 4:
            abc[x] = "\"#$%@\""
    phrase = " ".join(abc)
    return phrase


def bubble_sort(words):
    pass


# print(four_letters("all of the four letter words in this sentence have been replaced with \"#$%@\""))


def word_score(word_list):
    letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    letters = letters.split(" ")
    print(letters)
