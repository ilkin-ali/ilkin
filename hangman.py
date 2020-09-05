import random

print("H A N G M A N\n")
word_list = ['python', 'java', 'kotlin', 'javascript']
selected = random.choice(word_list)
i = 8
hidden = list('-' * len(selected))
while i > 0:
    str1 = "".join(hidden)
    print()
    print(str1)
    if str1 == selected:
        print("You guessed the word!")
        print("You survived!")
        break

    inp = input('Input a letter: ')
    if inp in selected:
        for j in range(len(selected)):
            if inp in hidden[j]:
                print("No improvements")
                i = i - 1
                break
            elif inp == selected[j]:
                hidden[j] = inp
    else:
        print("No such letter in the word")
        i = i - 1
else:
    print("You are hanged!")
