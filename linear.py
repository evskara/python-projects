import random

size = int(input("How many items to search through? "))

list = [random.randint(1, size) for _ in range(size)]
search = random.randint(1, size)

print(list)
print("Looking for:", search)

n = 0

def find_ordinal(num):
    j = num % 10
    k = num % 100

    if j == 1 and not k == 11:
        return str(num) + "st"
    elif j == 2 and not k == 12:
        return str(num) + "nd"
    elif j == 3 and not k == 13:
        return str(num) + "rd"
    else:
        return str(num) + "th"

for n in range(len(list)):
    if list[n] == search:
        print("Found in the", find_ordinal(n + 1), "position!")
        break
    else:
        n = n + 1
    
    if n == len(list):
        print("Not found...")
        break