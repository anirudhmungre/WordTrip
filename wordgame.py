import re
import random
import string

def isAnagram(str1, str2):
    str1_list = list(str1)
    str1_list.sort()
    str2_list = list(str2)
    str2_list.sort()

    return (str1_list == str2_list)

onlychars = re.compile('[^a-zA-Z]')
with open('wordlist.txt', 'r') as f:
    words = [line.strip().upper() for line in f if re.match('^[\w-]+$', line) is not None]

answers = []
while len(answers) < 2:
    scramble = "".join([random.choice(string.ascii_letters).upper() for x in range(0, random.randint(3, 5))])
    answers = [ans for ans in words if isAnagram(scramble, ans)]

print(scramble)
print(answers)

correct = []
while len(correct) != len(answers):
    guess = input("Enter a guess: ").strip().upper()
    if guess in answers:
        print("Correct!")
        correct.append(correct)
    else:
        print("Wrong!")
