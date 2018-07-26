# coding: utf-8
pizzas=['conghua', 'yangyou', 'jidanguan']
friend_pizzas = pizzas[:]
pizzas.append('pock')
friend_pizzas.append('milk')
print ("My favorate pizzas are: ")
for pizza in pizzas:
    print (pizza, end =' ')
    
print ("My friend favorate pizzas are: ")
for pizza in friend_pizzas:
    print (pizza, end =' ')
    
