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

for letters_in_word in range(len(list_Chosen_word)):
    hidden_word.append("_")
print(hidden_word)

while Guesses_Left > 0:
    users_pick = input("Pick a letter")
    Users_Guessed_letters.append(users_pick)
    print(Users_Guessed_letters)
    if users_pick in letters_in_word:
        hidden_word.append(users_pick)
    else:
        print("It is not in the word")
        Guesses_Left -= 1
    print(hidden_word)






