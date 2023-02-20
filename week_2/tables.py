from tabulate import tabulate

mydata = [
    ["Thyra" , "Nakuru"]
    ["Auria" , "Naivasha"]
    ["Auris" , "Taiyta Taveta"]
]
head =["Name" , "City"]
print(tabulate(mydata ,headers=head ,tablefmt="grid"))