# number to find the factorial of
number = 6

# start with our product equal to one
product = 1

# track the current number being multiplied
current = 1

while current <= number:  # write your while loop here

    product = product * current  # multiply the product so far by the current number

    current += 1  # increment current with each iteration until it reaches number

# print the factorial of number
print("factorial with while loop")
print(product)

print("\n")
#
print("factorial with for loop")
#
# number to find the factorial of
number = 6

# start with our product equal to one
product = 1

for number in range(1, number+1, 1):
   product = product * number


# print the factorial of number
print(product)