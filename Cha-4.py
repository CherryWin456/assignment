count=0
sen=input("write a string:")
n=len(sen)
for i in range(n):
    if sen[i] =="a" or sen[i]=="e" or sen[i]=="i" or sen[i]=="o" or sen[i]=="u":
            count=count+1
print("number of vowels:{}".format(count))



str_1=input("enter string:")
n=len(str_1)
a=b=i=0
c=d=0
for i in range(n):
    if str_1[i]>="A" and str_1[i]<="Z":
        a=a+1
    elif str_1[i]>="a" and str_1[i]<="z":
        b=b+1
for str in str_1:
    if str.isdigit():
        c=c+1
    elif str==" ":
        d=d+1
print("numbers of uppercase letters:",a)
print("numbers of lowercase letters:",b)
print("numbers of digits:",c)
print("numbers of whitespace characters:",d)



str=input("input a string:")
print(str[::-1])



info= {"name":"Thura" ,"birthday":"30-6-2003"}
def mainMenu():
    print("1.search information")
    print("2.add new information")
    print("3.change information")
    print("4.delete information")
    print("5.exit")
    choice=int(input("enter choice:"))
    loop=1
    while loop==1:   
            if choice==1:
                    name=str(input("enter name:"))
                    if name in info.values():
                        print ("birthday is",info["birthday"])
                    else:
                        print("name is not found")
                        
            if choice==2:
                    name=str(input("enter name:"))
                    birthday=str(input("enter birthday"))
                    if name in info.values():
                        print("already exist")
                    else:
                        
                        info["name1"]=name
                        info["birthday1"]=birthday
                        print(info)
                        
            if choice==3:
                    name1=str(input("enter name:"))
                    if name1 in info.values():
                        birthday=str(input("enter new birthday:"))
                        info["birthday"]=birthday
                    else:
                        print("name is not found")
                        
            if choice==4:
                    name1=str(input("enter name:"))
                    if name1 in info.values():
                        del info['name1']
                        del info["birthday"]
                        print(info)
                    else:
                        print("name is not found")
            elif choice==5:
                loop=0
            else:
                print("invalid choice,enter 1 to 5")
                mainMenu()
mainMenu()



list=[]
num=int(input("how many numbers in a list:"))
for i in range(num):
    number=int(input("enter number:"))
    list.append(number)
print(list)
list.sort()
print("largest number is",list[-1])

    






    
    









