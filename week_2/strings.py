#1 /usr/bin/ env python3

#This is a single line comment
#strings operations in python 
#Name :sharon
#Email : kokiemoto088@gmail.com
#date:17th Feb 2023
#File :strings.py

poem ="""this is a poem about nothing:
          its funny people laugh about nothing"""
print(poem)

f_name= "sharon"
s_name= "njoki"
full_name= f_name + s_name

age = 25 #years
'''print("my name is "+ full_name + " and i am" + str(age) + "years old")'''
print("my name is {} and i am {} years old" .format(full_name, age))


print
