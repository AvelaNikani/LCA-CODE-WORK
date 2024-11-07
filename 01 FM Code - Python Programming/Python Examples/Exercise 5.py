# Question 1: Creating and Modifying Lists

# TODO: Create a list of fruits
fruit_list = ["apple","banana","grapes","orange","pear"]
# TODO: Add a fruit to the end of the list
fruit_list.append("pineapple")
# TODO: Insert a fruit at the beginning of the list
fruit_list.insert(0,"grapefruit")
# TODO: Remove a fruit from the list
fruit_list.remove("banana")
# TODO: Print the modified list
print(fruit_list)
#-------------------------------------------------------------------------
# Question 2: List Operations

# TODO: Create a list of numbers from 1 to 5
number_list = [1,2,3,4,5]
# TODO: Create a new list with each number squared
squared_numbers = []
for i in number_list:
    squared_numbers.append(i**2)
print(squared_numbers)
# TODO: Find the sum and average of the original numbers
sums = sum(number_list)
mean = sums / len(number_list)
print(sums)
print(mean)
# TODO: Print the results
print(f"The numbers squared are {squared_numbers}")
print(f"The total of all the numbers is equal to {sums}")
print(f"The average for the number list is {mean}")

#-------------------------------------------------------------------------
# Question 3: Creating and Modifying Dictionaries

# TODO: Create a dictionary of countries and their capitals
countries_and_capitals = {"South Africa": "Pretoria","Brazil":"Rio de Janerio","New Zealand":"Christchurch","Egypt":"Cairo"}
# TODO: Add a new country-capital pair
countries_and_capitals.update({"Australia":"Perth"})
# TODO: Update the capital of an existing country
countries_and_capitals.update({"South Africa":"Bloemfontein"})
# TODO: Remove a country-capital pair
countries_and_capitals.pop("Brazil")
# TODO: Print the modified dictionary
print(countries_and_capitals)
#-------------------------------------------------------------------------
# Question 4: Dictionary Operations

# TODO: Create a dictionary of fruit colors
fruit_colors = {"orange":"orange","apple":"green","banana":"yellow","guava":"pink","pear":"green"}
# TODO: Print all the fruits (keys)
for fruit in fruit_colors.keys():
    print(fruit)
# TODO: Print all the colors (values)
for colors in fruit_colors.values():
    print(colors)
# TODO: Print each fruit and its color
for fruit,colors in fruit_colors.items():
    print(f"{fruit}={colors}")
# TODO: Check if a fruit is in the dictionary and print its color
print(fruit_colors["apple"])