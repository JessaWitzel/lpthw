
def fillthelist(x, y):
    i = 0
    numbers = []
    while i < x:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += y
        print("The list is:", numbers)
        print(f"At the bottom i is {i}")
    return numbers

def forloopforlist(x, y):
    i = 0
    numbers = []
    for num in range(i, x, y):
        print(f"At the top i is {i}")
        numbers.append(i)

        i += y
        print("The list is:", numbers)
        print(f"At the bottom i is {i}")
    return numbers

numbers = fillthelist(10, 2)
print("The numbers:")

for num in numbers:
    print(num)

fornumbers = forloopforlist(10, 2)
