import random 
upperc='ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
lowerc='abcdefghijklmnopqrstuvwxyz'
digitc='0123456789'
specialc='!@#$%^&*()_+<>?'

def add_upper():
  for i in range(li(i)):  
    password=''
    upper_case=int(input(f"how many uppercase letters to be in password #{i+1} :"))
    lower_case=int(input(f"how many lower case letters to be in password #{i+1}:"))
    digits=int(input(f"how many digits to be in password #{i+1}:"))
    special=l-upper_case-lower_case-digits
    if special>=0:
      print(f"Special characters to be in password #{i+1} is {special}")
      if li(i)>=3:
         add_upper()
      else:
         print("Your selected length for password is less than minimum length")
    else:
      print(f"Lol! your selection for lengths of Uppercase+Lowercase+Digits+special characters not equal to length l")
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

    passwords=''.join(char_list)
    print(passwords)            


print("The length of passwords should be minimum length of 3")
n=int(input("how many passwords do you want :"))
li=[]
for i in range(n):
   l=int(input(f"enter the length of password #{i+1}:"))
   li.append(l)

print("The password generation is executed sucessfully")   
