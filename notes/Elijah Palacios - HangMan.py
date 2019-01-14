import random
import string
word = ["hangman", "school", "math", "physicaleducation", "freshmen", "sophomore", "junior", "senior",
        "college", "food", "pizza", "smashbros", "dancing", "computers", "united"]
chosen_word = random.choice(word)
list_Chosen_word = list(chosen_word)
hidden_word = []
letters = list(string.ascii_lowercase)

for i in range(len(list_Chosen_word)):
    hidden_word.append("_")
print(hidden_word)

for i in range(8):
    for each_letter in list_Chosen_word:
        users_pick = input("Pick a letter")
        if users_pick == each_letter:
            current_index = hidden_word.index(users_pick)
            hidden_word.pop(current_index)
            hidden_word.insert(current_index, "")
            print(hidden_word)
            i += 1

