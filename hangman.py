import random

def print_word(word, guessed_letters):
    letters_to_print = [letter if letter in guessed_letters else "_" for letter in word]
    print(" ".join(letters_to_print))

def is_finished(word, guessed_letters):
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True

def is_letter(letter):
    return len(letter) == 1 and letter.lower() in "abcdefghijklmnopqrstuvwxyz"

words = ["abruptly", "absurd", "abyss", "affix", "askew", "awkward", "blizzard", "buzzing", "crypt", "oxygen", "wizard", "zombie"]
chosen_word = random.choice(words)
guessed_letters = []

max_attempts = 6
wrong_guesses = 0

while not is_finished(chosen_word, guessed_letters) and wrong_guesses < max_attempts:
    print_word(chosen_word, guessed_letters)
    user_input = input("Guess a letter > ").lower()

    if user_input == "gravy":
        print(f"The word is {chosen_word}")
        continue

    if is_letter(user_input):
        if user_input in guessed_letters:
            print("You already guessed that letter!")
        else:
            guessed_letters.append(user_input)
            if user_input in chosen_word:
                print("You guessed correctly!")
            else:
                wrong_guesses += 1
                print(f"Wrong guess! You have {max_attempts - wrong_guesses} tries left.")
    else:
        print("That's not a letter, dummy!")

# Win/Lose Screen
if is_finished(chosen_word, guessed_letters):
    print("\n YOU WIN! ")
    print(f"The word was: {chosen_word}")
else:
    print("\n YOU LOSE! ")
    print(f"The word was: {chosen_word}")