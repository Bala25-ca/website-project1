my_numbers = [10, 20, 30, 40, 50]

for i in range(4):
    my_numbers.insert(i, my_numbers[-1])

print(my_numbers)

alpha = [4, 8, 15, 16, 23, 42]
beta = alpha[:]
beta[2] = 99
print("Alpha:", alpha)
print("Beta:", beta)

#def compute_square(x):
    #return x * x


#def compute_quad(x):
    #return compute_square(x) * compute_square(None)


#print(compute_quad(4))

print(1//2)

my_values = [3 * i for i in range(5)]


def modify_list(values):
    del values[values[2] // 3]
    return values


print(modify_list(my_values))

x = 1
y = 2
x, y, z = x, x, y
z, y, z = x, y, z

print(x, y, z)

def custom_function(value):
    if value % 3 == 0:
        return 1
    else:
        return 2


print(custom_function(custom_function(4)))


inventory = ['apple', 'banana', 'cherry']
backup_inventory = inventory
del backup_inventory[:]

print("a", "b", "c", sep="sep")

#sample_tuple = (1, 2, 3)
#sample_tuple[0] = 5
#print(sample_tuple)

x = float(input("Enter a number: "))
y = float(input("Enter another number: "))
print(y ** (1 / x))

dictionary = {'alpha': 'beta', 'gamma': 'alpha', 'beta': 'gamma'}
value = dictionary['gamma']

for key in range(len(dictionary)):
    value = dictionary[value]

print(value)

def fun(x, y):
    if x == y:
        return x
    else:
        return fun(x, y-1)


print(fun(0, 3))

my_tuple = (10, 20, 30, 40, 50)
my_tuple = my_tuple[-3:-1]
my_tuple = my_tuple[-1]
print(my_tuple)

dct = {}
dct['1'] = (1, 2)
dct['2'] = (2, 1)

for x in dct.keys():
    print(dct[x][1], end="")

#print(3 + "5")

my_values = [3 * i for i in range(5)]


def modify_list(values):
    del values[values[2] // 3]
    return values


print(modify_list(my_values))
a = 1
b = 0
a = a ^ b
b = a ^ b
a = a ^ b

print(a, b)


#first_integer = int(input("Enter an integer: "))
#second_integer = int(input("Enter another integer: "))
#first_integer = first_integer % second_integer
#first_integer = first_integer % second_integer
#second_integer = second_integer % first_integer
# print(second_integer)

x = 1 // 5 + 1 / 5
print(x)

#sample_tuple = (1, 2, 3)
#sample_tuple[0] = 5
#print(sample_tuple)


#x = float(input())
#y = float(input())
#print(y ** (1 / x))

def fun(x, y):
    if x == y:
        return x
    else:
        return fun(x, y-1)


print(fun(0, 3))

my_dict = {"apple": 1, "banana": 2, "cherry": 3}

#for key in my_dict.keys():
 #   print(value, end="")
for value in my_dict.values():
   print(value)

matrix = [[x for x in range(3)] for y in range(3)]

count = 0
for row in matrix:
    for element in row:
        if element % 2 != 0:
            count += 1
print(count)

try:
    value = input("Enter a value: ")
    print(int(value)/len(value))
except ValueError:
    print("Bad input...")
except ZeroDivisionError:
    print("Very bad input...")
except TypeError:
    print("Very very bad input...")
except:
    print("Booo!")

foo = (1, 2, 3)
foo.index(0)

