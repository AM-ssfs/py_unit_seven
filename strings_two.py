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
    print(word_list)
    alpha = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    alpha = alpha.split(" ")
    score_total1 = []
    score_total2 = 0
    for word in range(len(word_list)):
        letter_list = []
        for letter in word_list[word]:
            letter_list.append(letter)
        for x in range(len(alpha)):
            while alpha[x] in letter_list:
                letter_list[letter_list.index(alpha[x])] = alpha.index(alpha[x])+1
        score_word = 0
        for y in range(len(letter_list)):
            score_word += letter_list[y]
        score_word = score_word*(word+1)
        score_total1.append(score_word)
        score_total2 += score_word
    print(score_total1)
    print(score_total2)
    return score_total2


word_score(["abc", "bbbz", "bcad", "a"])
