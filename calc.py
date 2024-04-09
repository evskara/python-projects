# Created 19/01/24
# Simple calculator

import time

def add_two_ints():
    print("What's the first integer?")
    int1 = int(input())
    print("And the second one?")
    int2 = int(input())
    int3 = int1 + int2
    print(int1,"+",int2,"=",int3)

def sub_two_ints():
    print("What's the first integer?")
    int1 = int(input())
    print("And the second one?")
    int2 = int(input())
    int3 = int1 - int2
    print(int1,"-",int2,"=",int3)

def mult_two_ints():
    print("What's the first integer?")
    int1 = int(input())
    print("And the second one?")
    int2 = int(input())
    int3 = int1 * int2
    print(int1,"x",int2,"=",int3)

def decimaldiv_two_ints():
    print("What's the first integer?")
    int1 = int(input())
    print("And the second one?")
    int2 = int(input())
    int3 = int1 / int2
    print(int1,"÷",int2,"=",int3)

def remdiv_two_ints():
    print("What's the first integer?")
    int1 = int(input())
    print("And the second one?")
    int2 = int(input())
    int3 = int1 // int2
    int4 = int1 % int2
    print(int1,"÷",int2,"=",int3,"with remainder",int4)

def calc():
    print("\nWelcome to the calculator. Please follow the instructions below:")
    time.sleep(1.75)
    print("What would you like to do? Type A to add, S to subtract, M to multiply and D to divide.")
    ans = input()
    if ans == "A" or ans == "a":
        add_two_ints()
    elif ans == "S" or ans == "s":
        sub_two_ints()
    elif ans == "M" or ans == "m":
        mult_two_ints()
    elif ans == "D" or ans == "d":
        print("Would you like your answer as a decimal or an integer with remainders? Type D for decimal, and R for remainder.")
        ans2 = input()
        if ans2 == "D" or ans2 == "d":
            decimaldiv_two_ints()
        elif ans2 == "R" or ans2 == "r":
            remdiv_two_ints()
        else:
            print("That's not an option.")
            calc()
    else:
        print("That's not an option.")
        calc()

calc()
