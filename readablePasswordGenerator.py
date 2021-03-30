import random

"""
_________________________________READABLE PASSWORD GENERATOR___________________________
Criteria:
1. Select a word
2. Select a special character
3. Select 2 integers

Get a random paragraph from wikipedia or something and add it to a text file

"""

wordlist = []
special_char = ['!', '@', '#', '$', '%', '^', '&', '*', '[', ']']

with open("Wikitext.txt", "r") as file:
    data = file.readlines()  # storing all lines in this var

    for line in data:
        words = line.split()  # Splitting the sentences into words

        for word in words:
            if len(word) > 5:
                wordlist.append(word.capitalize())  # Capitalizing each word in the list and appending to wordlist

word_char = random.choice(wordlist)
sp_char = random.choice(special_char)
num = str(random.randint(10, 99))  # type casting an int to str since we will be concatenating

passwd = word_char + sp_char + num
print(passwd)
