#one of the first programs I ever wrote, and also one of my most-used

import string
import random
import pyperclip

#using locally-dependent RNG
systemRandom = random.SystemRandom()
password = ''

length = int(input('Enter password length: '))

for i in range(length):
    password += systemRandom.choice(string.ascii_letters + string.digits + string.punctuation)

print(password)
pyperclip.copy(password)
