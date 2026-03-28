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

foods=[]
prices=[]
total=0
food=''
while food.lower()!='q':
 food=input(f'enter your food of the  ')
 if food!='q':
   price=float(input(f'enter your price of the :$ '))
   foods.append(food)
   prices.append(price)
for food in foods:
  print(food)
for price in prices:
  total+=price
  print(f'your total is :${total}')
 
    
    
  