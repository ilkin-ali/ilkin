cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
for city in cities:
    city = city.title()
    print(city)
print("Done!")

for index in range(len(cities)):
    cities[index] = cities[index].title()
print(cities)

# Creating a new list
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
capitalized_cities = []

for city in cities:
    capitalized_cities.append(city.title())
print(city)