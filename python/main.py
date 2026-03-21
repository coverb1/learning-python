# fist_name='mucyo bruce'
# email ="mucyobruce@gmail.com"
# number=44.4
# choose=True


#print(f'this is your email {email}')
#print(f'hello {fist_name}')

#using if statement

#is_student = True

#if is_student:
 #   print(f'{fist_name} you are student')
#   print(f'{fist_name} you are not student')
 
 #typecasting = the process of converting  a variable from one data type to another
 #str(), int(), float(),bool()

# email=bool(email)
# print(email)

#input()= A function that prompts the user to enter data returns the entered as string

#name=input('what is your name:?')
#age=input('what is your age:?')
#age=int(age)
#age=age+1
#print(f'hello {name}')
#print(f'your age is {age}')

#exercises 1 Rectangle Area caalc

# width=int(input('enter width:?'))
# length=int(input('enter width:?'))

# results=width*length

# print(f' this is your area {results}')

# exercise 2 creating cart 

# item=input('what  item would you like to buy?: ')
# price=int(input('what is the price:' ))
# quantity=int(input('how many quantity would you like:'))

# total=price*quantity
# print(f'the price you have to pay is :{total}')

# freinds=10
# freinds=freinds%2
# print(freinds)

# x=1.3
# y=2
# z=4

# results=min(x,y,z)
# print(results)
# import math
# a=float(input('enter the first number:'))
# b=float(input('enter the second number:'))
# results=math.sqrt(pow(a,2)+ pow(b,2))
# print(results)

# age=int(input('enter your age here: '))
# if age>=18 : 
#  print(f' you are allowed to vode {age}')
# elif age<=0:
#  print (f' you have not born yet {age}')
# else:
#  print(f' you are not allowed to vode {age}')

# name=input("enter your name here: ")
# if name=="":
#  print('you did not enter name')
# else:
#  print(f' hello {name}')

# oparator=input(' enter your oparator(+ - * /):')
# num1=float(input('enter firstNumber?: '))
# num2=float(input('enter secondNumber?: '))
# if oparator=='+':
#    result=num1+num2
#    print(result)
# if oparator=='-':
#    result=num1-num2
#    print (result)

# if oparator=='*':
#    result=num1*num2
#    print (result)

# if oparator=='/':
#    result=num1/num2
#    print (result)

#  condition expression
# X if condition else Y

# num=20
# print('enough' if num>20 else 'below') 

# phoneNumber=input('please enter your phone number here#: ')

# results=phoneNumber.replace('-',' ')
# print(results)

# validate user input

# username=input("enter your username here#:")
# resulst=len(username)
# if resulst>12 :
#  print('username is above 12')
# elif username.find(' ')!=-1:
#  print('username contains space')
# elif username.isdigit()!=True:
#  print('user name contains digits')
# else:
#  print(username)

# indexing
# we use []

# price1=3.1234

# print(f'{price1:.3f}')

# food=input('enter your food you like:')
# while food!='q':
#  print(f'hey you like {food}')
#  food=input('enter another food you like:')
# else:
#  print('byee')

# for loop
# for x in  range(1,20):
#   if x==13:
#    continue
#   else:
#    print(x)

import time

igihe=int(input('enter your time:'))
for x in range(0,igihe):
    second=x%60
    print(f'00:00:{second}')
    time.sleep(1)

print('it is time wake up')
    