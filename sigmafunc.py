from functools import reduce

#stolen tehe
def factors(n):
    return set(reduce(
        list.__add__,
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

#but this is all mine x
def sigma_function(num):
    return sum(factors(num))

usernum = int(input("Enter number: "))
print(sigma_function(usernum))

if sigma_function(usernum) == usernum * 2:
    print("The number is perfect!")
else:
    print("The number is not perfect.")