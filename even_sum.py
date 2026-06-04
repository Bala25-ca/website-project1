number = int(input("Enter a number: "))
for i in range(1, number + 1):
    if i % 2 == 0:
        sum = 0 + i
print(f"The sum of even numbers from 1 to {number} is: {sum}")


while True:
    number = int(input("Enter a number: "))
    if number < 0:
        print("Please enter a non-negative integer.")
        continue
    elif number % 2 == 0:
        sum = 0 + number
        print(f"The sum of even numbers from 1 to {number} is: {sum}")
    else:
        break