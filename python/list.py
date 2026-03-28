#collection in python
#collection single value used to store many things
 
#list=[]
#set={}
#tuple=()

# fruits=["apple","orange","banana","coconut"]
# print(fruits[0:3])
# for x in fruits:
#     print(x)
# fruits[0]="amanda"
# print(fruits)
# fruits.append('mucyo')
# fruits.remove('apple')
# fruits.insert(2,"mucyo")
#fruits.sort()
#fruits.reverse()

# print(fruits.index('apple'))

# fruits={"apple","orange","banana","coconut"}

#shopping cart

#foods=[]
#prices=[]
#total=0
#food=''
#while food.lower()!='q':
 #food=input(f'enter your food of the  ')
 #if food!='q':
 #  price=float(input(f'enter your price of the :$ '))
  # foods.append(food)
  # prices.append(price)
#for food in foods:
  #print(food)
#for price in prices:
 # total+=price
  #print(f'your total is :${total}')
 



# categories=({'apple','orange','banana','coconut'},
#          {'dodo','carrot','patatoes'},
#              {'inka','inkoko','ihene'}  )
# for categorie in categories:
#     for food in categories:
#         print(food, end='\n')
#     print()

# # print(categories[0][2])


# Quiz
# questions=('how many element are in periodic table:?',
# 'which animal lays  the largest leg?:',
# 'what is the most abundant gas in Earths atmosphere?: ',
# 'how many bones are in human  body:c',
# 'which planet in the solar system is the hotest')
  
# options=(("A.166","B.177","C.188","D.119"),
#          ("A.Whale","B.crocodile","C.Elephant","D.Ostrich"),
#          ("A.Nitrogen","B.Oxygen","C.Carbon-dioxide","D.Hydogen"),
#          ("A.206","B.207","C.208","D.209"),
#          ("A.Mercury","B.Venus","C.Earth","D.Mars"),
#          )

# answers=('C',"D","A","A","B")
# guesses=[]
# score=0
# question_num=0

# for question in questions:
#     print('-------------')
#     print(question)
#     for option in options[question_num]:
#         print(option)
#     guess=input("enter (A,B,C,D): ").upper()
#     guesses.append(guess)
#     if guess==answers[question_num]:
#         score+=1
#         print('CORRECT')
#     else:
#         print("INCORECT")
#         print(f'{answers[question_num]} is the correct answer')
#     question_num+=1

# print('______results______________')
# score=score/len(question)*100
# print(f'you score is {score}')

# dictonary a =a collection of  {key:value} pairs
# capital={'USA':'washington Dc','Rwanda':'Kigali'}
# capital.update({'Congo':'Kinshasa'})
# print(capital)
# print(capital.get('USA'))

menu={
    'banana':22,
    'cassava':33,
    'eggs':44,
    'juice':89
}
cart=[]
total=0

print('----------------MENU---------------------')
for key,values in menu.items():
    print(f'{key:10}:{values:.2f}')
print('----------------MENU---------------------')

while True:
    food=input('enter from MENU: ')
    if food=='q':
     break
    elif menu.get(food) is not None:
     cart.append(food)
     total+=menu.get(food)
print(cart)
print(total)