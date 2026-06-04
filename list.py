list = [1, 2, 3, 6, 7, 9, 11, 13, 15, 17, 19]
multiples_of_three = []
for n in list:
    if n % 3 == 0:
        multiples_of_three.append(n)
print(multiples_of_three)

counter = 1
while counter <=3:
    password = input("Enter a password: ")
    counter += 1
    if password == "python123":
        print("Password is valid.") 
        #print("Too many attempts")
        print("Access granted.")
    elif not any(char.isdigit() for char in password) or len(password) < 8 and counter != 4:
        print("Password length must be greater than 8 and contain at least one digit.")
        continue
    elif counter != 4:
        password = input("Enter a password: ")
        print("Too many attempts. Account locked.")
    break


