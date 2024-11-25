import random
from os.path import dirname
from random import randrange
from typing import List
from xml.sax.handler import property_interning_dict

print(dir(random))
'''x = int(input("Enter any year"))
if x:
    print("not a leap year")
elif:
    print("a leap year")'''

'''input_year = int(input("Enter a year:"))
def is_leap(year):
 if (input_year % 400==0) or (input_year % 4==0 and input_year % 100!=0):
        print("It is a leap year")
 else:
    print("It is not a leap year")'''

'''year = int(input("Enter a year: "))

if (year % 4 ==0 and year % 100 != 0) or year % 400 ==0:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")'''

'''age = int(input("Enter your age "))
height = int(input("Enter your height "))
bill=1000
bill=500
if (age<6, height<120 ):
    print("you cannot ride")
    if (age>18, height<120 ):
        print("you cannot ride")

if(age > 6, height > 120 ):
        print("you can ride,and your bill is 500")
elif (age>18, height>120 ):
    print("you can ride,and your bill is 1000")'''

'''age = int(input("Please enter your age: "))
height = int(input("PLease enter your height: "))
if ((age < 6 , age > 18) and height < 120):
        print("You cannot ride")
if ((age > 18, age == 18) and height > 120):
        print("You can ride, your bill is 1000$")
elif ((age > 6 , age < 18) and height > 120):
        print("You can ride, your bill is 500$")'''

'''age = int(input("Enter age: "))
height = int(input("Enter height: "))
bill = 0
if height > 120:
        print("Close enough")
        if age < 6:
                print("But cannot ride")
        elif age < 18:
                bill += 500
                print(f"You can ride, the bill's N{bill}")
        else:
                bill += 1000
                print(f"You can ride, the bill's N{bill}")
else:
        print("You cannot ride")'''

'''a = random. choice(["a","b","c","d","e","f"])
print(a)'''

'''b = random.randrange(0,11)
print(b)
if b % 2 ==0 :
        print("Is an even number")
else:
        print("Is an odd number")'''

'''user_dude = int(input("Enter a number ranging from 0-5: "))
b = random.randrange(0,6)
if user_dude==b:
        print(f"Dang bro you're a sicko, you're correct. the guess was {b}")
else:
        print(f"Mission failed, you're wrong. the guess was {b}")'''


'''y = ("red","blue","black","green","orange" )
for a in y:
    print(a)
new_y: list[str] = [a for a in y]
print(new_y)'''

'''num = (1,2,3,4,5)
for x in num:
    print(x)'''

'''val = (1,2,3,4,5)
y = 0
for num in val:
    y += num
    print(+y)'''

'''a = range(0,11)
for x in a:
    if x == 5:
        continue
    print(x)'''

'''a = range(0, 11)
for x in a:
    if x > 5:
        break
    print(x)'''


'''a = range(0,21)
for x in a:
    print(x)'''

'''a = range(0,21)
x=[x for x in a]
print(x)'''

'''a = range(21)
x = [x for x in a ]
print(x)
ff = [ x for x in range(21) if x % 2 == 0]
print(ff)'''

'''q = 0
while q <= 5 :
    print(f"{q} is less than 5 ")
    q += 1
else:
    print(f"{q} is more than 5")'''

'''user = input("Enter a password: ")

print("Re-enter your password ")
new_user = input("Enter a password: ")
while user != new_user:
    new_user = input("try again ")
else:
    print(f"""
               your password is {new_user}""")'''

'''''user = input("Enter a name: ")
email = input("Enter an email: ")

while user == (""):
    user = input("Invalid name, try again: " )
while "@" not in email :
    email = input("Invaild email, try again: " )
else:
    print(f"your name is {user} and your email is {email}")'''''

'''user = input("Enter username: ")
email = input("Enter email: ")

while (user == "") or ( "@" not in email):
    user = input("Invalid username,try username again: ")
    email = input("Invalid email,try email again: ")
print(f"Your username is {user}")
print(f"Your email is {email }")'''


'''user = input("Enter either: rock, paper, scissor : ")
a = random. choice(["rock","paper","scissor"])
print(a)
xx = 100
if (user == 'rock') and (a == 'rock') :
    print("Thats a tie")
if (user == 'paper') and (a == 'paper') :
    print("Thats a tie")
if (user == 'scissor') and (a == 'scissor') :
    print("Thats a tie")
if (user == 'rock') and (a == 'scissor'):
    xx += 50
    print("You've won")
if (user == 'rock') and (a == 'paper'):
    xx -= 10
    print("You've lost ")
if (user == 'scissor') and (a == 'rock'):
    xx -= 10
    print("You've lost")
if (user == 'scissor') and (a == 'paper'):
    xx += 50
    print("You've won")
if (user == 'paper') and (a == 'rock'):
    xx += 50
    print("You've won")
if (user == 'paper') and (a == 'scissor'):
    xx -= 10
    print("You've lost")
print(f"Your score is {xx}")'''


''''choices = ("rock","paper","scissors")
chances = 6
score = 100
rules = { "rock" : "scissors",
          "paper" : "rock",
          "scissors" : "paper"}

for trial in range(chances):
    if trial < chances :
        user_choice = input("Enter either rock, paper, scissors: ")
        if user_choice in choices:

            computer_choice = random.choice(choices)
            if user_choice == computer_choice:
                print(f"Its a tie. Your score is {score}")
            elif rules[user_choice] == computer_choice:
                score += 50
                print(f"Cool. Your score is {score} ")
            else:
                score -= 10
                print(f"Fool. your score is {score} ")
        else:
            print("choose either rock, paper, scissors ")
    else:
        print(f"GAME OVER... Your score is {score}")'''


'''x = range(101)
chances = 5
score = 100

for trial in range(chances):
    if trial < chances:
        user = input("Enter a number from 0 to 100: ")
        if user in x:

            computer_num = random.choice(x)
            if user == computer_num:
                score += 50
                print(f"correct, your score is {score}")
            else:
                score -= 10
                print(f"wrong, your score is {score}")

        else:
            print("Enter a number from 0 to 100 ")
    if user < computer_num:
        print(" a lil bit higher fowl")'''


'''answer = random.randint(1,100)
score = 100
chances = 5

for i in range(chances):
    user = int(input("Enter a number from 1 to 100: "))
    if user == answer:
        score += 50
        print(f"Correct your score is {score}")
        break
    elif user < answer :
        score -= 10
        print(f"That is incorrect u peasent, your score is {score} Try harder")
    else :
        score -= 10
        print(f"You foul creature you're wrong your score is {score}")
else:
    print(f"ok")'''



'''print(food)
print(food[-6])
pass
print(food[2:5])
print(food[1: ])
print(food[ :4])'''


'''if 'green' in colour:
    print("green is in colour ")
else:
    print("green is not in colour ")
if 'pink' in colour:
    print("pink is in colour ")
else:
    print("pink is not in colour")'''
'''colour = ("red", "black", "pink", "red", "orange", "purple", "white")
colour_1 =list(colour)
colour_1[0] = "green"
x =tuple(colour_1)
print(x)'''

'''colour += ("blue",)
print(colour)'''




'''food_1 =list(food)
food_1.remove("fish")
food = food_1
print(food)

c = colour+food
print(c)'''
'''food = ("yam", "rice", "fish", "meat", "egg", "bread", "fish",)
print(food)
print(dir(list))'''

'''a = ("pear","apple","pineapple")
(v_1, v_2, v_3) = a
print(v_1)
print(v_2)
print(v_3)'''

'''b = ("orange","mango","grape","apple","watermelon")
(v_1,v_2,v_3,v_4,v_5) = b
for i in b:
    print(i)
    print(len(b))

c = 2*b
print(c)
a = c.count("orange")
print(f"orange appears {a} times")
k = b.index("mango")
print(k)'''

"""user = (input("Enter your first name: "))
k = (input("Enter your last name: "))
name = (user, k)
print(name)"""



