num=int(input("enter a number:"))
if num%2==0:
    print("it's even")
else:
    print("it's an odd")



a=int(input("enter a integer:"))
b=int(input("enter another integer:"))
if a>b:
    print("the largest one is",a)
elif a==b:
    print("two are equal")
else:
    print("the largst one is",b)


a=int(input("enter first integer:"))
b=int(input("enter second integer:"))
c=int(input("enter third integer:"))
if a> b and a> c:
    print("largest one is",a)
elif b> a and b> c:
    print("largest one is",b)
elif c> a and c> b:
    print("largest one is",c)
else:
    print("they are equal")



year=int(input("enter a year:"))
if year%4==0:
    print(year,"is a leap year")
elif year%100==0:
    print(year,"is a leap year")
elif year%400==0:
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")



mar1=int(input("myanmar:"))
mar2=int(input("english:"))
mar3=int(input("mathematic:"))
ave=(mar1+mar2+mar3)//3
print(ave)
if 90<=ave<=100:
    print ("grade A")
elif 80<=ave<=89:
    print("grade B")
elif 70<=ave<=79:
    print("grade C")
elif 60<=ave<=69:
    print("grade D")
else :
    print("grade F")

    


