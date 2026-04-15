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
# Decoder
def decoder(message, keyword):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    full_keyword = (keyword * ((len(message) // len(keyword) + 1)))[:len(message)]
    decoded_words = []
    keyword_index = 0
    for word in message.split(" "):
        decoded_word = []
        for letter in word:
            if letter in alphabet:
                k = full_keyword[keyword_index]
                decoded_letter = alphabet[(alphabet.index(letter) + alphabet.index(k)) % 26]
                decoded_word.append(decoded_letter)
                keyword_index += 1
            else:
                decoded_word.append(letter)
        decoded_words.append("".join(decoded_word))
    return " ".join(decoded_words)
print(decoder("txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztcgcexxch!", "friends"))

# Encoder
def encoder(message, keyword):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    full_keyword = (keyword * ((len(message) // len(keyword) + 1)))[:len(message)]
    decoded_words = []
    keyword_index = 0
    for word in message.split(" "):
        decoded_word = []
        for letter in word:
            if letter in alphabet:
                k = full_keyword[keyword_index]
                decoded_letter = alphabet[(alphabet.index(letter) - alphabet.index(k)) % 26]
                decoded_word.append(decoded_letter)
                keyword_index += 1
            else:
                decoded_word.append(letter)
        decoded_words.append("".join(decoded_word))
    return " ".join(decoded_words)
print(encoder("your cryptography really stressed me out! i was overthinking a lot of things but i now see that it was all unnecessary.", "friends"))
