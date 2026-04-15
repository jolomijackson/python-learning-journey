"""Ceaser Cipher with 2 methods
Attempt 1"""
# Decoding function
def caeser_decode(message, offset):
    words = message.split(" ")
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    decoded_message = []
    for word in words:
        decoded_word = []
        for letter in word:
            if letter in alphabet:
                decoded_letter = alphabet[(alphabet.index(letter) + offset) % 26]
                decoded_word.append(decoded_letter)
            else:
                decoded_word.append(letter)
        decoded_message.append("".join(decoded_word))
    return " ".join(decoded_message)
print(caeser_decode("bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!", 14))

# Encoding function
def caeser_encode(message, offset):
    words = message.split(" ")
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    offset = 10
    decoded_message = []
    for word in words:
        decoded_word = []
        for letter in word:
            if letter in alphabet:
                decoded_letter = alphabet[(alphabet.index(letter) - offset) % 26]
                decoded_word.append(decoded_letter)
            else:
                decoded_word.append(letter)
        decoded_message.append("".join(decoded_word))
    return " ".join(decoded_message)
print(caeser_encode("", 10))

# Decoding without knowing offset
def caeser_decode(message, offset):
    words = message.split(" ")
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    decoded_message = []
    for word in words:
        decoded_word = []
        for letter in word:
            if letter in alphabet:
                decoded_letter = alphabet[(alphabet.index(letter) - offset) % 26]
                decoded_word.append(decoded_letter)
            else:
                decoded_word.append(letter)
        decoded_message.append("".join(decoded_word))
    return " ".join(decoded_message)
for num in range(0, 31):
    decoded = caeser_decode("vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.", num)
    print("Offset {}: {}".format(num, decoded))


"""Attempt 2"""
import string

# Encoder
def caeser_encrypt(message, offset):
    alphabet = string.ascii_lowercase
    new_letters = []
    for letter in message:
        if not letter in alphabet:
            new_letters.append(letter)
        else:
            letter_index = alphabet.index(letter)
            new_index = letter_index + offset
            new_letter = alphabet[new_index % 26]
            new_letters.append(new_letter)
    new_message = ''.join(new_letters)
    return new_message

# Decoder
def caeser_decrypt(message, offset):
    alphabet = string.ascii_lowercase
    new_letters = []
    for letter in message:
        if not letter in alphabet:
            new_letters.append(letter)
        else:
            letter_index = alphabet.index(letter)
            new_index = letter_index - offset
            new_letter = alphabet[new_index % 26]
            new_letters.append(new_letter)
    new_message = ''.join(new_letters)
    return new_message
