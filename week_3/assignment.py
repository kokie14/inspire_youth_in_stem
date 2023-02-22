h= eval(input("enter diamonds height:"))

for x in range (h):
    print(" " * (h-x),"*" * (2*x + 1))
for x in range (h - 2,-1,-1):
    print(" "* (h-x),"x"* (2*x + 1))



from math import factorial
#input n
n =5
for i in range (n):
    for j in range (n-i + 1):
        print(end= "")
for i in range (n):
    for j in range (n-i + 1):
        print(factorial(i)// (factorial(j)* factorial(i-j)),end="")




        