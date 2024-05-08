import random 
import string
upperc='ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
lowerc='abcdefghijklmnopqrstuvwxyz'
digitc='0123456789'
specialc='!@#$%^&*()_+<>?'
password=[]
def add_upper(upper_case,upperc,password):
    for i in range(1,upper_case):
        up=random.choice(upperc)
        password=password+up
      

def main():
    print("The length of passwords should be minimum length of 3")
    n=input("how many passwords do you want")
    upper_case=input("uppercase letters to be in password")
    lower_case=input("how many lower case letters to be in password")
    digits=input("how many digits to be in password")
    special=input("how many special characters to be in password")
    if len(upper_case+lower_case+digits+special)!=0:
        print("your selection for length of password does not matches with inputs")
        


main()  