

from ast import While
import numbers

x = int(input("Please enter a number between 35-100"))



if 35 <= x <= 1000:
    if x>= 100:
        print("100")

    else:
        while x <= 100:
            if x % 2 == 0:
                print(x)
            x+=1




else:
    print("Enter a valid number")

