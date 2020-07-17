print("WE NEED\nTO LEARN PYTHON\nAS QUICKLY AS POSSIBLE")
#####
print("\n")
#####
given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

name_length = len(given_name)+len(middle_names)+len(family_name)+2
#todo: calculate how long this name is

# Now we check to make sure that the name fits within the driving license character limit
# Nothing you need to do here
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)

#####
print("\n")
#####
mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"
weekly_sales = int(mon_sales) + int(tues_sales) + int(wed_sales) + int(thurs_sales) + int(fri_sales)
weekly_sales = str(weekly_sales)  #convert the type back!!
print("This week's total sales: " + weekly_sales)