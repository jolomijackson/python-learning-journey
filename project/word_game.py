# Module code: typer.py
"""Plays a game where the user types random words within a time limit."""

import random
import time
import word_bank

def play_level_one(words, seconds):
    """Returns True if the user successfully completed the round."""
    # Run a stopwatch for the time it takes the user to respond.
    start = time.time()
    response = input("(" + str(seconds) + " seconds) " + words + "\n")
    stop = time.time()

    # Fail the round if a word is mispelled or if time runs out.
    within_time_limit = stop - start < seconds
    return response == words and within_time_limit

def hangman(num, word):
    """Returns random word with blank spaces"""
    num_revealed_letters = num
    revealed_letters = random.sample(range(len(word)), num_revealed_letters)
    display = ""
    for i, letter in enumerate(word):
        if i in revealed_letters:
            display += letter
        else:
            display += "_"
    return display

def play_level_two(num, word):
    """Returns True if user successfully completed the round."""
    display = hangman(num, word)
    attempts = 0
    strike = 1
    while attempts < 3:
        print("Guess the word: " + display)
        response = input("~> ").lower()
        if response == word:
            break
        else:
            print("Strike " + str(strike) + "!")
            strike += 1
        attempts += 1
    return response == word
    
def pick_random_words(num_words, word_length):
    """Returns a random phrase containing the given number of words.""" 
    words = ""
    for word in range(num_words):
        word = get_random_word(word_length)
        words = words + " " + word

    return words.strip()

def get_random_word(mode):
    """Returns a random word with a word length based on the given mode."""
    if mode == "hard":
        words = word_bank.hard_words
    elif mode == "medium":
        words = word_bank.medium_words
    else:
        words = word_bank.easy_words

    return random.choice(words)


# Main file: main.py
import typer
import time

"""Level 1
Play three rounds of a speed typing game."""
def level_one():
    print("Type the words and hit enter within the time limit!")
    for round_num in range(1, 4):
        print("Round " + str(round_num))
    
        words_to_type = typer.pick_random_words(round_num, "easy")
        passed = typer.play_level_one(words_to_type, 10)
        if not passed:
            break
    return passed

"""Level 2
Play a hangman game with 3 tries"""
def level_two():
    print("\n Level 2! \n")
    print("Guess the word in 3 tries!")
    for round_num in range(3):
        print("Round " + str(round_num + 1))
        
        word = typer.get_random_word("medium")
        passed = typer.play_level_two(4, word)
        if not passed:
            print("The word is " + word)
            break
    return passed

"""Level 3
# Harder hangman game with timer"""
def level_three():
    print("\n Level 3! \n")
    print("Guess the word in 3 tries within the time limit!")
    for round_num in range(3):
        print("Round " + str(round_num + 1))
        word = typer.get_random_word("medium")
        
        start = time.time()
        passed = typer.play_level_two(4, word)
        stop = time.time()
        
        time_taken = stop - start 
        passed = passed and time_taken <= 30
        if not passed:
            print("The word is " + word)
            break
    return passed

"""Level 4
# Hangman game with harder words"""
def level_four():
    print("\n Level 4! \n")
    print("Guess the word in 3 tries!")
    for round_num in range(3):
        print("Round " + str(round_num + 1))
        
        word = typer.get_random_word("hard")
        passed = typer.play_level_two(7, word)
        if not passed:
            print("The word is " + word)
            break
    return passed

"""Level 5
# Hangman game with harder words and timer"""
def level_five():
    print("\n Level 5! \n")
    print("Guess the word in 3 tries within the time limit!")
    for round_num in range(3):
        print("Round " + str(round_num + 1))
        word = typer.get_random_word("hard")
        
        start = time.time()
        passed = typer.play_level_two(8, word)
        stop = time.time()
        
        time_taken = stop - start 
        passed = passed and time_taken <= 30
        if not passed:
            print("The word is " + word)
            break
    return passed

levels = [level_one, level_two, level_three, level_four, level_five]
for i, level in enumerate(levels):
    passed = level()
    if not passed:
        print("Level failed :( You reached level " + str(i + 1) + " out of 5!")
        break
else:
    print("Congratulations! You completed all 5 levels!")
        
print("Thanks for playing.")


# Word bank: word_bank.py
"""Lists of words with varying lengths and difficulties."""

easy_words = [
    "bat",
    "dog",
    "toy",
    "cat",
    "rat",
    "law",
    "mud",
    "boy",
    "the",
    "she",
    "red",
    "pop",
    "lie",
    "bay",
    "hay",
    "can",
    "sad",
    "mad",
    "cap",
    "rap",
    "met",
    "fad",
    "hop",
    "top",
    "tap",
    "lap",
    "lie",
    "bag",
    "ham",
    "ray",
    "say",
    "tie",
    "bit",
    "hit",
    "hat",
    "bet",
    "bid",
    "lid",
    "pad",
    "and",
    "tan",
    "tar",
    "eat",
    "ate",
    "lag",
    "rag",
    "tag",
    "kid",
    "dip",
    "rip",
    "lip",
    "pod",
    "rod",
    "nod",
    "his",
    "sis",
    "gem",
    "ant",
    "wad",
    "win",
    "nap",
    "way",
    "pay",
    "day",
    "van",
    "mom",
    "dad",
    "dot",
    "rot",
    "tip",
    "hen",
    "tin",
    "fee",
    "pee",
    "tee",
    "tea",
    "pea",
    "bee",
    "sea",
    "see",
    "men",
    "man",
    "did",
    "sim",
    "pin",
    "fib",
    "yay",
    "may",
    "pot",
    "pan",
    "run",
    "ran",
    "ton",
    "put",
    "hut",
    "but",
    "cut",
    "pit",
    "vat",
]

medium_words = [
    "lemon",
    "cheese",
    "happy",
    "angry",
    "tomato",
    "carve",
    "tattoo",
    "water",
    "walks",
    "visit",
    "liver",
    "flight",
    "height",
    "skirts",
    "house",
    "train",
    "spoon",
    "tiger",
    "zebra",
    "doctor",
    "teach",
    "study",
    "juice",
    "bottle",
    "never",
    "peace",
    "donor",
    "python",
    "coding",
    "uncle",
    "sleeps",
    "table",
    "wonder",
    "growth",
    "forest",
    "river",
    "yellow",
    "purple",
    "cycle",
    "pillow",
    "school",
    "queen",
    "yogurt",
    "bouncy",
    "flavor",
    "guitar",
    "piano",
    "breeze",
    "sunny",
    "window",
    "marvel",
    "gloves",
    "framed",
    "sweet",
    "dirty",
    "clean",
    "apple",
    "coffee",
    "button",
    "refer",
    "climb",
    "minute",
    "light",
    "shelf",
    "wobble",
    "tired",
    "party",
    "brain",
    "vault",
    "tennis",
    "winter",
    "cover",
    "paper",
    "pencil",
    "hello",
]

hard_words = [
    "congratulations",
    "absolutely",
    "photosynthesis",
    "monstrosity",
    "university",
    "cheeseburger",
    "accommodate",
    "suburban",
    "pizazz",
    "assuming",
    "stewardess",
    "xylophone",
    "overzealous",
    "withdrawal",
    "wednesday",
    "vulnerable",
    "visualization",
    "versatile",
    "veterinary",
    "vaccination",
    "vegetarian",
    "unanimous",
    "transmission",
    "trajectory",
    "temporary",
    "tournament",
    "temperature",
    "surveillance",
    "psychology",
    "responsibility",
    "recommendation",
    "pronunciation",
    "practitioner",
    "plagiarism",
    "pilgrimage",
    "philosophy",
    "participation",
    "nutritious",
    "necessarily",
    "miscellaneous",
    "marshmallows",
    "mayonnaise",
    "leprechaun",
    "limousine",
    "kindergarten",
    "knowledgeable",
    "interference",
    "inflammation",
    "handkerchief",
    "fluorescent",
    "extraordinary",
    "pharmaceutical",
    "exhiliration",
    "environmental",
    "disappointment",
    "choreography",
    "circumstantial",
    "cauliflower",
    "cantaloupe",
    "auditorium",
    "apostrophe",
    "amphitheater",
    "advantageous",
    "acknowledgement",
    "abbreviation",
    "abundant",
    "accommodation",
    "adjustment",
    "ambidextrous",
    "asymmetrical",
    "auxiliary",
    "bachelorette",
    "bureaucracy",
    "behavioral",
    "boulevard",
    "camouflage",
    "determination",
    "differentiation",
    "description",
    "dysfunctional",
    "impressionable",
    "enthusiastic",
    "entrepreneur",
    "eavesdropping",
    "exaggerated",
    "fascinating",
    "governmental",
    "hygienic",
    "immediately",
    "individuality",
    "interpretation",
    "laboratory",
    "labyrinth",
    "lieutenant",
    "lightning",
    "legitimate",
    "likelihood",
    "maintenance",
    "masquerade",
    "medicinal",
    "mezzanine",
    "medieval",
    "mischievious",
    "misunderstood",
    "pneumonia",
    "noticeable",
    "opportunity",
    "overwhelming",
    "picturesque",
    "pilgrimage",
    "prohibitive",
    "quadruple",
    "ridiculous",
    "sacrilegious",
    "rudimentary",
    "chandelier",
    "sophomore",
    "superfluous",
    "susceptible",
    "suspicious",
    "synonymous",
    "tomorrow",
    "zucchini",
]
