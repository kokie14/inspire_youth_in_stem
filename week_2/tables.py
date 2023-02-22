
from tabulate import tabulate
data = [["mavs",99],
        ["suns",91],
        ["spurs",94],
        ["nets",88]]

col_names = ["teams","points"]
print(tabulate(data,headers=col_names,tablefmt="fancy_grid"))