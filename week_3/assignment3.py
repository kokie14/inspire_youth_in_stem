n =8 
for i in range (n):
    print('' * (n-i),end= '')
    print(''.join (map(str,str(11 ** i))))  


n=5;i=0
while(i<=n):
    print(" " * (n-1)+ "*" * i )
    i+=1