# numbers = [1, 2, 3]
#
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#
# new_list.append(add_1)

#sau

# new_list = [n + 1 for n in numbers]

# List comprehension:

# new_list = [new_item for item in list]

# Conditional list comprehension:

# new_list = [new_item for item in list if test]



# list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# numbers = [int(n) for n in list_of_strings]
# result = [n for n in numbers if n % 2 == 0]
# print(result)



#Dictionary comprehension:

#new_dict = {new_key:new_value for item in list}

#new_dict = {new_key:new_value for (key, value) in dict.items()}

#new_dict = {new_key:new_value for (key, value) in dict.items() if test}

# student_dict = {
#     "student" : ["Angela", "James", "Lily"],
#     "score" : [56, 76, 98]
# }

#Looping through dictionaries:

# for (key, value) in student_dict.items():
#     print(value)

import pandas

# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

#Looping through a data frame:

# for (key, value) in student_data_frame.items():
#     print(value)

#Loop through rows of a data frame

# for (index, row) in student_data_frame.iterrows():
#     # print(row)
#     # print(row.score)
#     if row.student == "Angela":
#         print(row.score)

# Keyword Method with iterrows():

# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()
output_list = [nato_dict[letter] for letter in word]
print(output_list)