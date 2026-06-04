grade = int(input("Enter the student's grade: "))
if grade >= 90:
    print("Your Grade is: A")
    print("Excellent work! Keep it up!")
elif grade >= 80 and grade < 90:
    print("Your Grade is: B")
elif grade >= 70 and grade < 80:
    print("Your Grade is: C")
elif grade >= 60 and grade < 70:
    print("Your Grade is: D")
else:
    print("Your Grade is: F")
    print("Try harder next time!")
