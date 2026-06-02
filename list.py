list = [1, 2, 3, 6, 7, 9, 11, 13, 15, 17, 19]
multiples_of_three = []
for n in list:
    if n % 3 == 0:
        multiples_of_three.append(n)
print(multiples_of_three)