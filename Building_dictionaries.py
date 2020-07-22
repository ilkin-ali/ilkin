book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_counter = {}
for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] += 1
print(word_counter)
What's happening here?
#The for loop iterates through each element in the list. For the first iteration, word takes the value 'great'.
#Next, the if statement checks if word is in the word_counter dictionary.
#Since it doesn't yet, the statement word_counter[word] = 1 adds great as a key to the dictionary with a value of 1.
#Then, it leaves the if else statement and moves on to the next iteration of the for loop. word now takes the value expectations and repeats the process.
#When the if condition is not met, it is because thatword already exists in the word_counter dictionary, and the statement word_counter[word] = word_counter[word] + 1 increases the count of that word by 1.
#Once the for loop finishes iterating through the list, the for loop is complete.

#ikinci yolu da budur

#for word in book_title:
  #  word_counter[word] = word_counter.get(word, 0) + 1
#print(word_counter)

