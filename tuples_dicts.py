# Tuples and Dictionaries
from unicodedata import name


tuple_month = ("January", "February", "March", "April", "May", "June",
         "July", "August", "September", "October", "November", "December")
print(tuple_month[0])
print(tuple_month[-1])
try:
    tuple_month[0]="New Month"
    print(tuple_month[0])
except:
    print("Tuples are immutable, error: <error_message>")

my_dict = {"Joe": "grade A", "Jane": "grade B", "John": "grade C"}
for i in range(len(my_dict.items())):
    name, value = list(my_dict.items())[i]
    my_dict[name] = value
print(my_dict)
my_dict["Jack"] = "grade D"
print(my_dict)
my_dict.update({"Jill": "grade E"})
print(my_dict)
my_dict["Jack"] = "grade A+"
print(my_dict)









