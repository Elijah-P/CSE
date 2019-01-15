import random
import string
word = ["Hangman", "school", "math", "physicaleducation","Freshmen", "Sophomore", "Junior", "Senior", "college", "food",
        "pizza", "Mr.Wiebe", "Smashbros", "dancing", "computers", "United States" "I am late for class"]
Guesses_Left = 8
Chosen_Word = random.choice(word)
list_Chosen_word = list(Chosen_Word)
letters = list(string.ascii_lowercase)
hidden_word = []
Users_Guessed_letters = []

while Guesses_Left > 0:
    for letters_in_word in range(len(list_Chosen_word)):
        hidden_word.append("_")
        print(hidden_word)
        users_pick = input("Pick a letter")
        if users_pick == list_Chosen_word.index(0):
            hidden_word.append(list_Chosen_word.index(0))
            print(hidden_word)
        Users_Guessed_letters.append(users_pick)
        print(Users_Guessed_letters)
        Guesses_Left -= 1
