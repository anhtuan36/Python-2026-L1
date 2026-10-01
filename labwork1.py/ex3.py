
import math
n = int(input("Enter an integer n: "))

if n < 2:
    print(f"{n} is not a prime number")
else:
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            print(f"{n} is not a prime number")
            break
    else:
        print(f"{n} is a prime number")