age = int(input("Enter your age: "))
if age < 18:
    print("You are a minor.")
elif age > 18 and age < 21:
    print("You are a young adult.")
else:
    print("You are an adult.")