# You would like to count the number of fruits in your basket.
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits, but you do not want to count the other items in your basket.

#Example 1

result = 0
basket_items = {'pears': 5, 'grapes': 19, 'kites': 3, 'sandwiches': 8, 'bananas': 4}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

for object, count in basket_items.items(): #Iterate through the dictionary
    if object in fruits:
        #if the key is in the list of fruits, add the value (number of fruits) to result
        result = count + result



print("There are {} fruits in the basket.".format(result))

#Example 2

result = 0
basket_items = {'peaches': 5, 'lettuce': 2, 'kites': 3, 'sandwiches': 8, 'pears': 4}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

for object, count in basket_items.items(): #Iterate through the dictionary
    if object in fruits:
        #if the key is in the list of fruits, add the value (number of fruits) to result
        result = count + result



print("There are {} fruits in the basket.".format(result))

print("\n")
#
#
print("example 3\n")

result = 0
basket_items = {'lettuce': 2, 'kites': 3, 'sandwiches': 8, 'pears': 4, 'bears': 10}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']
for object, count in basket_items.items(): #Iterate through the dictionary
    if object in fruits:
        #if the key is in the list of fruits, add the value (number of fruits) to result
        result = count + result



print("There are {} fruits in the basket.".format(result))
#
print("\n")
#
#
print("example 4\n")
#
You would like to count the number of fruits in your basket.
In order to do this, you have the following dictionary and list of
fruits.  Use the dictionary and list to count the total number
of fruits and not_fruits.

fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

for object, count in basket_items.items():
  if object in fruits:
      fruit_count += count
  else:
      not_fruit_count += count


#if the key is in the list of fruits, add to fruit_count.

#if the key is not in the list, then add to the not_fruit_count


print("The number of fruits is {}.  There are {} objects that are not fruits.".format(fruit_count, not_fruit_count))