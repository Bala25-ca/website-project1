print("Hello, World!")
print("Welcome to Python programming.")
print('''This is a multi-line string in Python.''')
print('Python is a versatile language used for various applications.')
print("Let's learn Python together!\n It's fun and rewarding.")
print("""We're just ordinary people
We don't know which way to go, yeah, hey
'Cause we're ordinary people
Maybe we should take it slow, hey, hey
We're just ordinary people
We don't know which way to go
'Cause we're ordinary people
Maybe we should take it slow""")
print("Python is great for data analysis, web development, and automation.", end="")
print(" It has a large community and many libraries to choose from.")
print("My", "name", "is", "JamesBond", sep="-")
print("This is the first line.", end="\n")
print("My", "name", "is", "JamesBond", sep="*")
print('''This is a multi-line string in Python. It can span multiple lines without needing special characters.''')
print(True > False)
print(True < False)
print(2 > 1)
print(2 + 3)
print(10 - 5)
print(4 * 5)
print(20 / 4)
print(20 // 3)
print(20 % 3)
print(2 ** 3)
print(10 > 5 and 5 > 3)
print(9 % 6 % 2)
name = "JamesBond"
age = 30
height = 1.75
print("My name is", name, "and I am", age, "years old.")
# Adding new value to age
age = age + 5
print("My name is", name, "and I am", age, "years old.")
name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
height = float(input("Enter your height is: "))
print("Hello your name is", name, "and you are", age, "years old. Your height is", height, "meters.")
width = 5.5
height = 2
print("The area of the rectangle is", width * height)
name = "James + Bond"
print(name)
name = "James" * 3
print(name)
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
print("The result is:", float(result))
