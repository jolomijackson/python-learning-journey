"""Two approaches for the Vigenere Cipher
Approach 1:"""
import string

# Encoder
def vigenere_encrypt(message, keyword):
    alphabet = string.ascii_lowercase
    new_letters = []
    counter = 0

    for letter in message:
        if letter in alphabet or letter.isupper():
            letter_lower = letter.lower()
            letter_index = alphabet.index(letter_lower)
            keyword_index = alphabet.index(keyword[counter % len(keyword)])
            new_index = letter_index + keyword_index
            new_letter = alphabet[new_index % 26]
            if letter.isupper():
                new_letter = new_letter.upper()
            new_letters.append(new_letter)
            counter += 1
        else:
            new_letters.append(letter)
            
    new_message = ''.join(new_letters)
    return new_message

# Decoder
def vigenere_decrypt(message, keyword):
    alphabet = string.ascii_lowercase
    new_letters = []
    counter = 0

    for letter in message:
        if letter in alphabet or letter.isupper():
            letter_lower = letter.lower()
            letter_index = alphabet.index(letter_lower)
            keyword_index = alphabet.index(keyword[counter % len(keyword)])
            new_index = letter_index - keyword_index
            new_letter = alphabet[new_index % 26]
            if letter.isupper():
                new_letter = new_letter.upper()
            new_letters.append(new_letter)
            counter += 1
        else:
            new_letters.append(letter)
    new_message = ''.join(new_letters)
    return new_message


"""Approach 2:"""
