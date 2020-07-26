letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for num, letter in zip(letters, nums):
    print("{}: {}".format(letter, num))

letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)



print("\nQuiz: Zip Coordinates")
#
#Use zip to write a for loop that creates a string specifying the label and coordinates of each point and appends it to the list points.
# Each string should be formatted as label: x, y, z. For example, the string for the first coordinate should be F: 23, 677, 4.

x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
# write your for loop here
for point in zip(labels, x_coord, y_coord, z_coord):
    points.append("{}: {}, {}, {}".format(*point))

for point in points:
    print(point)


print("\nQuiz: Transpose with Zip")
#Use zip to transpose data from a 4-by-3 matrix to a 3-by-4 matrix.
# There's actually a cool trick for this! Feel free to look at the solutions if you can't figure it out.
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = tuple(zip(*data))# replace with your code
print(data_transpose)