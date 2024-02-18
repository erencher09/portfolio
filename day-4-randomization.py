
# import random

# random_integer = random.randint(1, 10)
# print(random_integer)

# random_float = random.random()
# print(random_float)


# random_number = random_integer*random_float

# print(random_number)

# states_of_america = ["Delaware", "Pennsylvania"]

# print(states_of_america[1])

# states_of_america.extend(["Beans", "Turtles"])

# print(states_of_america)


# names = names_string.split(", ")
# # The code above converts the input into an array seperating
# #each name in the input by a comma and space.

# import random

# num_items = len(names)
# random_integer = random.randint(0, num_items - 1)
# payer = names[random_integer]

# print(f"{payer} is going to buy the meal today!")


# fruits = ["Strawberry", "Mangos"]
# vegetables = ["Tomato", "Celery"]

# fruits_veggies = [fruits, vegetables]

# print(fruits_veggies)

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index=int(position[1]) - 1
map[number_index][letter_index] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")