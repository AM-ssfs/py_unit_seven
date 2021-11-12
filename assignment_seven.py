_alphabet_ = "abcdefghijklmnopqrstuvwxyz"


def ask_encode_decode():
    '''
    returs true if user is encoding
    returns false if user is decoding
    :return:
    '''
    while True:
        user_input = input("do you want to encode (\"1\") or decode (\"2\") or quit (\"q\") ")
        if user_input == "1":
            return True
        elif user_input == "2":
            return False
        elif user_input.upper() == "Q":
            print("Goodbye :)")
            exit()
        else:
            print("please enter \"1\" or \"2\" or \"q\"")


def format_text(text):
    '''
    removes all spaces
    makes lowercase
    makes into list
    :param text:
    :return:
    '''
    text = text.lower()
    while " " in text:
        text = text[:text.index(" ")] + text[text.index(" ")+1:]
    text = list(text)
    return text


def letter_number(letters):
    '''
    takes a sting of letters and makes it into a list
    then takes that list and turns letters into numbers
    :param letters:
    :return:
    '''
    alphabet = _alphabet_
    alphabet = list(alphabet)
    for x in range(len(alphabet)):
        while alphabet[x] in letters:
            letters[letters.index(alphabet[x])] = x
    return letters


def number_letter(numbers):
    alphabet = _alphabet_ + _alphabet_
    alphabet = list(alphabet)
    for x in range(len(numbers)):
        numbers[x] = alphabet[numbers[x]]
    return numbers


def add_lists(list1, list2):
    list3 = []
    for x in range(len(list1)):
        list3.append(list1[x]+list2[x])
    return list3


def subtract_lists(list1, list2):
    list3 = []
    for x in range(len(list1)):
        list3.append(list1[x] + 26 - list2[x])
    return list3


def get_message():
    message = input("What is the message you want to encode/decode? (ONLY USE LETTERS, NO PUNCTUATION!) ")
    return message


def get_key():
    key = input("What is the key you want to encode/decode with? (ONLY USE LETTERS, NO PUNCTUATION!) ")
    return key


def key_len(message, key):
    while True:
        if len(key) >= len(message):
            return key
        else:
            key += key


def encode_decode(user, message, key):
    message = format_text(message)
    key = format_text(key)
    message = letter_number(message)
    key = letter_number(key)
    key = key_len(message, key)
    if user:  # encode
        encoded = add_lists(message, key)
    else:  # decode
        encoded = subtract_lists(message, key)
    encoded = number_letter(encoded)
    encoded = ''.join(encoded)
    print(encoded)
    return encoded


def main():
    user = ask_encode_decode()
    message = get_message()
    key = get_key()
    return encode_decode(user, message, key)


if __name__ == '__main__':
    main()



