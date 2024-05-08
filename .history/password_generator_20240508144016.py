import random 
upperc='ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
lowerc='abcdefghijklmnopqrstuvwxyz'
digitc='0123456789'
specialc='!@#$%^&*()_+<>?'
all=upperc+lowerc+digitc+specialc

def add_upper(li()):
   password_required=[]
   for i in range(n):
      password=''
      for j in range(li(i)):
         addition=random.choice(all)
         password=password+addition
      char_list=list(password)
      random.shuffle(char_list)
      shuffled_password=''.join(char_list)
      password_required.append(shuffled_password)
      print(f"password #{i+1} = {password_required(i)}")
   
li=[]
print("Minimum length of password should be 3")
print("How many passwords do you want to generate?")
n=int(input())
for i in range(n):
   l=int(input(f"enter the length of password #{i+1}:"))
   li.append(l)
add_upper()   

   
         

