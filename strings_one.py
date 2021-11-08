def half_slice(word):
    num = int(len(word)/2)
    front = word[:num]
    back = word[num:]
    word2 = back + front
    return word2


def no_first_last(str):
    word = ""
    for x in range(1, len(str)-1):
        word += str[x]
    return word


def longest(phrase):
    words = phrase.split(" ")
    big = 0
    for x in range(len(words)):
        long = len(words[x])
        if big < long:
            big = long
    return big



def title_case(sentence):
    pass


longest("ada asdaf ad")