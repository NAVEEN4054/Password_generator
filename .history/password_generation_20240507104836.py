import random 
upperc='ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
lowerc='abcdefghijklmnopqrstuvwxyz'
digitc='0123456789'
specialc='!@#$%^&*()_+<>?'
password=""
i=1
def add_upper():
    password=''
    for i in range(upper_case):
        up=random.choice(upperc)
        password=password+up
    for i in range(lower_case):
        lo=random.choice(lowerc)
        password=password+lo
    for i in range(digits):
        di=random.choice(digitc)
        password=password+di
    for i in range(specialc):
        sp=random.choice(specialc)
        password=password+sp
    print(password)            


print("The length of passwords should be minimum length of 3")
n=input("how many passwords do you want")
upper_case=int(input("uppercase letters to be in password"))
lower_case=int(input("how many lower case letters to be in password"))
digits=input("how many digits to be in password")
special=input("how many special characters to be in password")
add_upper()

