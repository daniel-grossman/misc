#one of the first programs I ever wrote, and also one of my most-used

import random
import string

#using an OS-dependent cryptographic RNG source
systemrandom = random.SystemRandom()

#'all' is a string of all possible letters, numbers etc.
all = string.ascii_letters + string.digits + string.punctuation

#these lists store password lengths + passwords
lengths = []
passwords = []

#user input for num. of passwords
numPass = int(input('Enter number of passwords: '))

#user input for length of each password
for i in range(0, numPass):
    print('Enter password no. {} length: '.format(i+1))
    lengt = int(input())
    lengths.append(lengt)

#password creation using each length
for i in lengths:
    password = ''.join(systemrandom.choices(all, k=i))
    passwords.append(password)

for i in passwords:
    print(i)
