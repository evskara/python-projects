import time

length = int(input("What number would you like the program to run up to?: "))
delay = float(input("How long would you like the program to wait until it prints the next number?: "))

for i in range(length + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
        time.sleep(delay)
        continue
    
    if i % 5 == 0 and i % 3 != 0:
        print("buzz")
        time.sleep(delay)
        continue

    if i % 3 == 0 and i % 5 != 0:
        print("fizz")
        time.sleep(delay)
        continue

    print(i)

    time.sleep(delay)

def find(num):
    if num % 3 == 0 and num % 5 == 0:
        print(f"{num} would be: fizzbuzz.")
    
    if num % 5 == 0 and num % 3 != 0:
        print(f"{num} would be: buzz.")

    if num % 3 == 0 and num % 5 != 0:
        print(f"{num} would be: fizz.")

    if num % 3 != 0 and num % 5 != 0:
        print(f"{num} would be neither fizz nor buzz.")


time.sleep(3)

print("You can also use this to search through and find what a number would be. What number would you like to find?")
ans = int(input())

find(ans)

# i think i did it yayyyy but its not very good awww but it works yayyyy