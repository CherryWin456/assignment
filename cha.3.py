num=int(input("enter a number:"))
for i in range(1,13):
    print(num,"x",i ,"=",num*i)


    
factorial=1
num=int(input("enter a number:"))
if num<0:
    print("factorial does not exist")
elif num==0:
    print("factorial is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
print("factorial is",factorial)



num=int(input("enter a positive integer:"))
sum_of_digit=sum(int(digit) for digit in str(num))
print(sum_of_digit)



num=int(input("enter number:"))
string=str(num)
if string==string[::-1]:
    print("it is palindrome")
else:
    print("it is not palindrome")



a=int(input("enter first number:"))
b=int(input("enter second number:"))
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
print( gcd(a,b))