import random
import string
word = ["Hangman", "school", "math", "physicaleducation","Freshmen", "Sophomore", "Junior", "Senior", "college", "food",
        "pizza", "Mr.Wiebe", "Smashbros", "dancing", "computers", "United States" "I am late for class"]
Guesses_Left = 8
Chosen_Word = random.choice(word)
list_Chosen_word = list(Chosen_Word)
hidden_word = []
letters = list(string.ascii_lowercase)
Users_Guessed_letters = []

for i in range(len(list_Chosen_word)):
    hidden_word.append("_")
print(hidden_word)

while Guesses_Left > 0:
    for each_letter in list_Chosen_word:
        users_pick = input("Pick a letter")
        Users_Guessed_letters.append(users_pick)
        if users_pick == each_letter:
            current_index = hidden_word.index(users_pick)
            hidden_word.pop(current_index)
            hidden_word.insert(current_index, "")
            print(hidden_word)
            Guesses_Left -= 1

