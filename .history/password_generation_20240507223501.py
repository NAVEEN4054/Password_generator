import random 
upperc='ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
lowerc='abcdefghijklmnopqrstuvwxyz'
digitc='0123456789'
specialc='!@#$%^&*()_+<>?'

def add_upper():
  for k in range(n):   
    upper_case=int(input(f"how many uppercase letters to be in password #{k+1} :"))
    lower_case=int(input(f"how many lower case letters to be in password #{k+1}:"))
    digits=int(input(f"how many digits to be in password #{k+1}:"))
    special=l-upper_case-lower_case-digits
    if special>=0:
      print(f"Special characters to be in password #{k+1} is {special}")
    else:
      print(f"Lol! your selection for lengths of Uppercase+Lowercase+Digits+special characters not equal to length l")  
    passwords=[]
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
    for i in range(special):
        sp=random.choice(specialc)
        password=password+sp
    char_list=list(password)
    random.shuffle(char_list)

    passwordsp=''.join(char_list)
    passwords.append(passwordsp)
  for i in range(n):
   print(f"password #{i+1} : {passwords(i)}")   
  
print("The length of passwords should be minimum length of 3")
n=int(input("how many passwords do you want :"))
li=[]
for i in range(n):
   l=int(input(f"enter the length of password #{i+1}:"))
   li.append(l)
add_upper()
print("The password generation is executed sucessfully")
