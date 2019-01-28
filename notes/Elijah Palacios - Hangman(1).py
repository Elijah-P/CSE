import random
import string
word = ["Hangman.", "School", "Math", "Physical Education", "Freshmen.", "Sophomore", "Junior", "Senior", "College",
        "Pizza", "Mr.Wiebe", "Smashbros.", "Dancing", "Computers", "United States", "Am late for class?",
        "U.S.A", "This is Mr.Wiebe's computer."]
Guesses_Left = 8
Chosen_Word = random.choice(word)
list_Chosen_word = list(Chosen_Word)
Users_Guessed_letters = []
punctuation = [".", "'", "?", " "]
exclude_punctuation = []
users_pick = ""

# Build exclusive word
for letter in list_Chosen_word:
    if letter in string.ascii_letters + " ":
        exclude_punctuation.append(letter)

while Guesses_Left > 0:
    # Hides / Reveal Letters based on user guesses
    hidden_word = []
    for letter in list_Chosen_word:
        if letter.lower() not in Users_Guessed_letters and letter not in punctuation:
            hidden_word.append("_ ")
        else:
            hidden_word.append(letter)

    if hidden_word == list_Chosen_word:
        print(Chosen_Word)
        print("You win!")
        Guesses_Left = 0
        continue
    if users_pick.lower() == Chosen_Word.lower():
        print(Chosen_Word)
        print("You win!")
        Guesses_Left = 0
        continue
    print("".join(hidden_word))

    # Ask for input
    users_pick = input("Pick a letter").lower()
    Users_Guessed_letters.append(users_pick)
    print(Users_Guessed_letters)

    # Check to see if the letters are in the word
    if users_pick not in list_Chosen_word:
        Guesses_Left -= 1
        if Guesses_Left == 0:
            print("You lose")
