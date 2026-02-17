#Functions with outputs

# def my_function():
#     result = 3 * 2
#     return result

#output = result

def format_name(f_name, l_name):
  print(f_name.title())
  print(l_name.title())
format_name("ANGELA", "angela")

def format_name(f_name, l_name):
  format_f_name = f_name.title()
  format_l_name = l_name.title()
  print(f"{format_f_name} {format_l_name}")
format_name("AnGeLa", "YU")

def format_name(f_name, l_name):
  format_f_name = f_name.title()
  format_l_name = l_name.title()
  return f"{format_f_name} {format_l_name}"
format_string = format_name("AnGeLa", "YU")
print(format_string)

def format_name(f_name, l_name):
  format_f_name = f_name.title()
  format_l_name = l_name.title()
  return f"{format_f_name} {format_l_name}"
print(format_name("AnGeLa", "YU"))

#Storing output in a variable

formatted_name = format_name(input("Your first name: "), input("Your last name: "))
print(formatted_name)

#or printing output directly

print(format_name(input("What is your first name? "), input("What is your last name? ")))

#Already used functions with outputs

length = len(formatted_name)

#Return as an early exit

def format_name(f_name, l_name):
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs."
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  f"Result: {formated_f_name} {formated_l_name}"

#Exercitiu

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
  
# TODO: Add more code here 👇
def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if month == 2 and is_leap(year):
    return 29
  else:
      return month_days[month - 1]
#🚨 Do NOT change any of the code below 
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)



#Docstrings

"""_summary_"""

def format_name(f_name, l_name):
  """Take a first and last name and format it 
  to return the title case version of the name."""
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs."
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"Result: {formated_f_name} {formated_l_name}"



#Calculator

#simplu

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide,
}

num1 = int(input("What's the first number?: "))

for symbol in operations:
  print(symbol)
operation_symbol = input("Pick an operation from the line above: ")

num2 = int(input("What's the second number?: "))

calculation_function = operations[operation_symbol]

answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")



#complet

from art_calculator import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)
  num1 = float(input("+"))
  for symbol in operations:
    print(symbol)
  should_continue = True
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()