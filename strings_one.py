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
    sentence.lower()
    words = sentence.split(" ")
    for x in range(len(words)):
        first = words[x][0:1]
        first = first.upper()
        rest = words[x][1:]
        words[x] = first+rest
    sentence2 = " ".join(words)
    return sentence2


title_case("this is a sentence")

