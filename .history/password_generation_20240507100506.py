import random 
upperc='ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
lowerc='abcdefghijklmnopqrstuvwxyz'
digitc='0123456789'
specialc='!@#$%^&*()_+<>?'
password=""
i=1
def add_upper():
    for i in range(upper_case):
        up=random.choice(upperc)
        password=password+up
def add_lower():
    for i in range(lower_case):
        lo=random.choice(lowerc)
        password.append(lo)
def add_digit():
    for i in range(digits):
        di=random.choice(digitc)
        password.append(di)
def add_special():
    for i in range(specialc):
        sp=random.choice(specialc)
        password.append(sp)
print("The length of passwords should be minimum length of 3")
n=input("how many passwords do you want")
upper_case=int(input("uppercase letters to be in password"))
lower_case=input("how many lower case letters to be in password")
digits=input("how many digits to be in password")
special=input("how many special characters to be in password")
add_upper()
add_lower()
add_digit()  
add_special()
print(password)