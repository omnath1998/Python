rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

l = [rock, paper, scissors]

a = input(
    "Choose Your Input\n\n(print 'r' for rock\n\nprint 'p' for paper\n\nprint 's' for scissors):"
)
print()

if a == 'r':
    print(rock)
elif a == 'p':
    print(paper)
elif a == 's':
    print(scissors)
else:
    print('choose properly!')
print()
print('Computers Action: ')

import random

b = l[random.randint(0, 2)]
print(b)

if a == 'r':
    if b == paper:
        print('You Loose!')
    elif b == scissors:
        print('You Win!')
    else:
        print('Draw!')

elif a == 'p':
    if b == scissors:
        print('You Loose!')
    elif b == rock:
        print('You Win!')
    else:
        print('Draw!')

elif a == 's':
    if b == rock:
        print('You Loose!')
    elif b == paper:
        print('You Win!')
    else:
        print('Draw!')
