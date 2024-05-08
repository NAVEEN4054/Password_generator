import random 
upperc='ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
lowerc='abcdefghijklmnopqrstuvwxyz'
digitc='0123456789'
specialc='!@#$%^&*()_+<>?'
i=1
def add_upper():
  for i in range(n):  
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

    passwords=''.join(char_list)
    print(passwords)            


print("The length of passwords should be minimum length of 3")
n=int(input("how many passwords do you want :"))
l=int(input("enter the length of password to be generated :"))
upper_case=int(input("how many uppercase letters to be in password :"))
lower_case=int(input("how many lower case letters to be in password :"))
digits=int(input("how many digits to be in password :"))
special=l-upper_case-lower_case-digits
if special>=0:
   print(f"Special characters to be in password is {special}")
   if l>=3:
      add_upper()
   else:
      print("Your selected length for password is less than minimum length")
else:
   print(f"your selection for lengths of Uppercase+Lowercase+Digits+special characters not equal to length l  i.e.,{upper_case+lower_case+digits+special!=l}")
print("The password generation is executed sucessfully")   
