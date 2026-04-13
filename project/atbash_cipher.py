import string

def atbash_cipher(message):
    alphabet = string.ascii_lowercase
    backwards = ''.join(reversed(alphabet))
    
    new_letters = []
    for letter in message:
        if not letter in alphabet:
            new_letters += letter
        else:
            letter_index = alphabet.index(letter)
            new_letter = backwards[letter_index]
            new_letters += new_letter
    
    new_message = "".join(new_letters)
    return new_message
