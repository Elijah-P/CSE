import random
import string
word = ["hangman", "school", "math", "physicaleducation", "name", "freshmen", "sophomore", "junior", "senior",
        "college", "food", "pizza", "kerry", "delaney", "wiebe", "smashbros", "dancing", "computers", "united"]
chosen_word = random.choice(word)
list_Chosen_word = list(chosen_word)
letters = string.ascii_lowercase
users_pick = input("Pick a letter")

for i in range(len(list_Chosen_word)):
    

for each_letter in list_Chosen_word:
        if users_pick == each_letter:
            current_index = list_Chosen_word.index(users_pick)
            list_Chosen_word.pop(current_index)
            list_Chosen_word.insert(current_index, "*")
print(list_Chosen_word)