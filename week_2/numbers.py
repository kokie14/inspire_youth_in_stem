numbers =[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

sum_num=0
for number in numbers:
    number=int(input("Enter the first 17 numbers:"))
    sum_num = sum_num + number

avg_num=sum_num/17
print(avg_num)