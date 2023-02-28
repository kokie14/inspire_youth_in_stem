try:
    f= open('C:\Users\Ganchanja\Documents\Inspire_youth_IN_STEM\week_4\test.txt','r+w')
except:
    print()

#exception handling
filename= 'test.txt'
try:
    for file in filename:


file1 =open("test.txt")
print(file1.read())
file1.close()