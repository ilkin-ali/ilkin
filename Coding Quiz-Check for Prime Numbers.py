check_prime = [26, 39, 51, 53, 57, 79, 85]

# iterate through the check_prime list
for num in check_prime:

# search for factors, iterating through numbers ranging from 2 to the number itself
    for i in range(2, num):

# number is not prime if modulo is 0
        if (num % i) == 0:
            print("{} is NOT a prime number, because {} is a factor of {}".format(num, i, num))
            break

# otherwise keep checking until we've searched all possible factors, and then declare it prime
        if i == num -1:
            print("{} IS a prime number".format(num))

"""Question: Write code to check if the numbers provided in the list check_prime are prime numbers.
# For each number, if the number is prime, the code should print that the number is a prime number.
# If the number is NOT a prime number, it should print that the number is not a prime number,
# and also print a factor of that number besides 1 and the number itself.

#Logic for our solution:

#We loop through each number in the check_prime list.
#Create a "search-for-factors" loop beginning at 2, and continuing up to the (number-1)
#Use a conditional statement with themodulo operator to check if our number when divided by the possible factor yields any remainder besides 0.
#If we ever find one factor, we can declare that the number is not prime, and state the factor we found. Then we can break out of the loop for that number.
#If we get up to the (number - 1) and haven't broken out of the loop, then we can declare that the number is prime."""