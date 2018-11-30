import random
import string
word = ["hangman", "school", "math", "physicaleducation", "name", "freshmen", "sophomore", "junior", "senior",
        "college", "food", "pizza", "kerry", "delaney", "wiebe", "smashbros", "dancing", "computers", "united"]
chosen_word = random.choice(word)
list_Chosen_word = list(chosen_word)
hidden_word = []
letters = string.ascii_lowercase

for i in range(len(list_Chosen_word)):
    hidden_word.append("*")
print(hidden_word)

for i in range(8):
    for each_letter in list_Chosen_word:
        users_pick = input("Pick a letter")
        if users_pick == each_letter:
            current_index = hidden_word.index(users_pick)
            hidden_word.pop(current_index)
            hidden_word.insert(current_index, "")
            print(hidden_word)