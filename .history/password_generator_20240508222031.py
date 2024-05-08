import random 
upperc='ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
lowerc='abcdefghijklmnopqrstuvwxyz'
digitc='0123456789'
specialc='!@#$%^&*()_+<>?'
all=upperc+lowerc+digitc+specialc

def add_upper():
   password_required=[]
   for i in range(n):
     password=''
     if li(i)!=0:
      for j in range(li[i]):
         addition=random.choice(all)
         password=password+addition
      char_list=list(password)
      random.shuffle(char_list)
      shuffled_password=''.join(char_list)
      password_required.append(shuffled_password)
      print(f"password #{i+1} = {password_required[i]}")
     else:
        print(f"spooky choice! length of password of #{i+1} is less than minimum length ") 
li=[]
print("Minimum length of password should be 3")
n=int(input("How many passwords do you want to generate?"))
for i in range(n):
   l=int(input(f"enter the length of password #{i+1}:"))
   if l>=3:
      li.append(l)
   else:
      li.append(0)   
add_upper()
   
         

