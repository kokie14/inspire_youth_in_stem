
from tabulate import tabulate
data = [["mavs",99],
        ["suns",91],
        ["spurs",94],
        ["nets",88]]

col_names = ["teams","points"]
print(tabulate(data,headers=col_names,tablefmt="fancy_grid"))


from tabulate import tabulate
data= [["marie", 21],
       ["utah",65],
       ["noir",72],
       ["aaron",34]]

col_names=["names","points"]
print(tabulate(data,headers=col_names,tablefmt="fancy_grid"))