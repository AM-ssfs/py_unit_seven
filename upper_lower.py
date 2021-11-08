def get_input():
    return str(input("Say something: "))


def write(word):
    print(word.upper())
    print(word.lower())


def letters_in(word):
    for x in range(len(word)):
        print(word[x])


def main():
    word = get_input()
    write(word)
    letters_in(word)


if __name__ == '__main__':
    main()