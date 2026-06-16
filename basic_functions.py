name = str(input("What is your name? "))
def greet_user(name):
    print("Hello! welcome, " + name + "!")
greet_user(name)

# Add 2 numbers with a function
def add_numbers(num1, num2):
    return num1 + num2
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
result = add_numbers(number1, number2)
print("The sum of", number1, "and", number2, "is:", result)
#result = add_numbers(5, 10)
add_numbers(number1, number2) 

# Check if a number is even with a function
def is_even(number):
    return number % 2 == 0

# Test the function
test_number = float(input("Enter a number to check if it's even: "))
if is_even(test_number):
    print(test_number, "is even.")
else:
    print(test_number, "is not even.")

