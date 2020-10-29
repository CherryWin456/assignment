list=[]
num=int(input("enter how many numbers in a list:"))
for i in range(num):
    number=int(input("enter number:"))
    list.append(number)
print("sum:",sum(list))



list=[]
num=int(input("how many nunbers:"))
for u in range(num):
    number=int(input("enter number:"))
    list.append(number)
def unique(list):
    unique_list=[]
    for i in list:
        if i not in unique_list:
            unique_list.append(i)
    for i in unique_list:
        print(i, end=" ")
print("unique list is",unique(list))




for i in range(1,6):
    print("*"*i)




a=int(input("enter variable:"))
b=int(input("enter another variable:"))
def add(a,b):
    return a+b
c=(add(a,b))
print("sum:",c)
def substracted(a,b):
    return a-b
c=(substracted(a,b))
print("substruction:",c)
def multiply(a,b):
    return a*b
c=(multiply(a,b))
print("multiplication:",c)
def divided(a,b):
    return a//b
c=(divided(a,b))
print("division:",c)


    
    

