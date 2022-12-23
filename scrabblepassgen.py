#dumb password generator using scrabble dictionary, eventually want
#to mathematically estimate likliehood of guessing password first try without using computer
#WARNING: THIS CAN BE BRUTE-FORCED, DO NOT USE FOR ACTUAL PASSWORD MAKING

from random import SystemRandom
from csv import reader
import os

#os.chdir('') insert directory
sysrand = SystemRandom()

wordList, delisted = [], []
punctuation = [",", ".", "?", "!", ":", ";", "-","'"]

#getting all the words
with open('dictionary.csv', mode = 'r') as file:
    words = reader(file)

    for word in words:
        wordList.append(word)

#making all the words into a list of strings
for word in wordList:
    stringedWord = ''.join(word)
    delisted.append(stringedWord)
    
#enter num. of wanted passwords
n = int(input('Enter number of passwords: '))
k = int(input('Enter minimum password length: '))

#generation
for i in range(n):
    password = ''
    while len(password) <= k:
        if sysrand.random() > 0.5:
            password += sysrand.choice(punctuation)
        else:
            password += sysrand.choice(delisted)
    print(password)
