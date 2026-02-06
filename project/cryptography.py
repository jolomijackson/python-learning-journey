## Ceaser Cipher
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

## Vigenere Cipher
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
