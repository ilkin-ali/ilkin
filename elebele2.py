import random
print("H A N G M A N")
list = ['python', 'java', 'kotlin', 'javascript']
random.seed()
guess = random.choice(list)
user_input = input("Guess the word: ")
if user_input == guess:
    print('You survived!')
else:
    print('You are hanged!')