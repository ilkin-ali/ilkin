elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
print(elements["helium"])  # print the value mapped to "helium"
elements["lithium"] = 3  # insert "lithium" with a value of 3 into the dictionary
#
print("\n")
#

print("carbon" in elements)
print(elements.get("dilithium"))
print(elements)
#
print("\n")
#

n = elements.get("dilithium")
print(n is None)
print(n is not None)
m=elements.get('kryptonite', 'There\'s no such element!')
print(m)

#
print("\n")
#

population = {'Shangai': 17.8,
'Istanbul':13.3,
'Karachi':13,
'Mumbai': 12.5}
print(population)