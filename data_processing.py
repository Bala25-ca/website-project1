

from itertools import count
import math
import numbers

def average_of_list(numbers):
    try:
        if not numbers:
            return "Cannot calculate the average of an empty list."
        return sum(numbers) / len(numbers)
    except zeroDivisionError:
        return "Cannot calculate the average of an empty list."
numbers_list = [10, 20, 30, 40, 50]
average = average_of_list(numbers_list)
print("The average of the list is:", average)




my_dict = {"math": 100, "science": 80, "history": 70, "math": 100}
def average_of_math(d):
    try:
        if not d:
            return "Cannot calculate the average of an empty dictionary."
        else:
            values = [v for k, v in d.items() if k == "math"]
            avg = sum(values)/len(values)
            print("The average of the math scores is:", avg)
        return sum(d.values()) / len(d)
    except zeroDivisionError:
        return "Cannot calculate the average of an empty dictionary."
average_dict = average_of_math(my_dict)
print("The average of allscores is:", average_dict)
