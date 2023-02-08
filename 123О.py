from random import randint
b = randint(1,3)
print("Ножницы - 1")
print("Камень - 2")
print("Бумага - 3")
a = int(input() )
print(b)
if a == 1:
   if b == 1:
    print("ничья")
   elif b == 2:
    print("вы проиграли")
   else:
    print("вы выйграли")   
elif a == 2:
   if b == 1:
    print("Выграли")
   elif b == 2:
    print("ничья")
   else:
    print("вы проиграли")  
else:
   if b == 1:
    print("проиграли")
   elif b == 2:
    print("вы выграли")
   else: 
    print("вы ничья")  