import random
import string
word = ["Hangman", "School", "Math", "Physical Education", "Freshmen", "Sophomore", "Junior", "Senior", "College",
        "Pizza", "Mr.Wiebe", "Smashbros", "Dancing", "Computers", "United States", "I am late for class"]
Guesses_Left = 8
Chosen_Word = random.choice(word)
list_Chosen_word = list(Chosen_Word)
letters = list(string.ascii_lowercase)

Users_Guessed_letters = []


while Guesses_Left > 0:
    # Hides / Reveal Letters based on user guesses
    hidden_word = []
    for letter in list_Chosen_word:
        if "." in letter:
            current_index = list_Chosen_word.index(".")
            hidden_word.insert()

        if letter.upper() not in Users_Guessed_letters:
            hidden_word.append("_ ")
        else:
            hidden_word.append(letter)

    print("".join(hidden_word))
    if hidden_word == list_Chosen_word:
        Guesses_Left = 0
        continue

    # Ask for input
    users_pick = input("Pick a letter")
    Users_Guessed_letters.append(users_pick)
    print(Users_Guessed_letters)


    # Check to see if the letters are in the word
    if users_pick not in list_Chosen_word:
        Guesses_Left -= 1


