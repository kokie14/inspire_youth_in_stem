#write a program that calculates 16%
#ranging between 100k - 150k

# 10%tax income is between 150k - 300k
#30% tax income is above 300k
#5% if income is less 100k

#print gross income ,net income





income=input("enter your net income")

gross_income=int(input("what is your gross income?"))

tax_group_a=(gross_income*0.01)
tax_group_b=(gross_income*0.16)
tax_group_c=(gross_income*0.19)
tax_group_d=(gross_income*0.3)

if gross_income < 100000:
    print("gross_income:",gross_income)
    print("tax=", tax_group_a)
    print("net_income:",gross_income-tax_group_a)
elif( gross_income >100001) &( gross_income < 150000):
    print("gross_income:",gross_income)
    print("tax=", tax_group_b)
    print("net_income:",gross_income-tax_group_b)
elif(gross_income<=150001) & (gross_income<= 300000):
     print("gross_income:",gross_income)
     print("tax=", tax_group_c)
     print("net_income:",gross_income-tax_group_c)
    
elif (gross_income> 300000):
    print("gross_income=",gross_income)
    print("tax=", tax_group_d)
    print("net_income:",gross_income-tax_group_d)
    




