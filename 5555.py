a=int(input(" "))
new_a=0
for i in range(len(str(a))):
    new_a=a%10+new_a
    new_a=new_a*10
    a=a//10
print(new_a//10)