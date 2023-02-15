a=(int(input("Введите число: ")))
b=0
c=0


for i in  range(len(str(a))):
    if a%2==0:
        c=c+1
    else:
        b=b+1
    a=a//10
print("Нечетных чисел",b)
print("Четных чисел",c)
