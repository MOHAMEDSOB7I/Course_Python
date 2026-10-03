#First App
""" 
user_name = input("Please Enter Your Name: ")
age = input("Please Enter Your Age: ")
print(f"Welcom {user_name} your age is {age}")
"""

#Second App
""" 
f_number = input("Enter The first number: ")
s_number = input("Enter The second number: ")
print(f"Total={float(f_number) + float(s_number)}")
"""

#if & else
""" 
Number = 10
Name = "Mohamed"
if Number >= 10 and Name == "Mohamed":
    print("This Number is equal more than 10 and Name equal Mohamed")
else:
    print("This Number is less than 10")
"""

#system 
""" 
grade = int(input("What is your score: "))
#0-100
if grade < 0 or grade > 100:
    print("Invalid Value")
#90-100 -> excellent a
elif grade >=90:
    print(f"Your Grade Is {grade} - excellent - Grade A")
#70-90 -> very good
elif grade >=70:
    print(f"Your Grade Is {grade} - very good - Grade B")
#50-70 -> good
elif grade >=50:
    print(f"Your Grade Is {grade} - very good - Grade C")
#0-50 -> failed 
else:
    print(f"Your Grade Is {grade} - Needs Improvrment - failed")
"""

""" 
name = "Mohamed Sobhi"
print(name.upper())
print(name.find("S"))
print(name[-1])
print(len(name))
if "M" in name:
    print("Yas")
else:
    print("No")
"""

""" 
Num = [4,3,1,0,6,5]
Num.sort()
cart = ["Phone" , "Laptop" , "TV"]
cart.extend(Num)
#New_Product = input("Enter a New product: ")
#remove_Product = input("Name product: ")
#cart.remove(remove_Product)
#cart.append(New_Product)
#cart.clear()
print(cart)
"""
#--------------------------------------(2-10-2026)-----------------------------------------#

#list ["",""] , tuple , set , dict

#While loop
""" 
i = 0
while i <= 100:
    print(i)
    i+=1
else:
    print("End loop")
names = ["ali" , "mohamed" , "sara"]
i = 0
while i < len(names):
    print(names[i])
    i+=1
"""
#For loop
""" 
names = ["Mohamd", "Ali" , "Ahmed" , "Sara"]
input_name = input("enter your name: ")
for number in range(4):
    if input_name == names[number]:
        print(names[number])
        break
    else:
        print(names[number], f"Is not {input_name}")
"""

"""  
for i in names:
    print (i)

for Num in range(10,50,2):
    print(Num)
"""

#Function 
"""  
def say_hello(name):
    print("Hello ",name)
say_hello("Mohame")
say_hello("Ahmed")
say_hello("Ali")
"""

def calc(num1 , num2):
    return num1 + num2

result = calc(5,5)*2
print(result)