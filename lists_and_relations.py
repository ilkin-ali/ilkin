list_of_random_things = [1, 3.4, 'a string', True]
print(list_of_random_things[0])

print("\n")
print(list_of_random_things[len(list_of_random_things) - 1])
print(list_of_random_things[-1])

print("\n")
print(list_of_random_things[1:2])
print(list_of_random_things[:2])
print(list_of_random_things[1:])

print("\n")
print('this' in 'this is a string')
print('isa' in 'this is a string')

print("\n")
my_lst = [1, 2, 3, 4, 5]
my_lst[0] = 'one'
print(my_lst)

print("\n")
month = 8
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
num_days=days_in_month[month-1]
#use list indexing to determine the number of days in month
print(num_days)

print("\n")
eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']
# TODO: Modify this line so it prints the last three elements of the list
print(eclipse_dates[-3:])

print("\n")
sentence1 = "I wish to register a complaint."
sentence2 = ["I", "wish", "to", "register", "a", "complaint", "."]
sentence2[6]="!"
print(sentence2)