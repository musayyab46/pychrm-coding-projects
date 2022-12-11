str1=input("enter date1:")
str2=input("enter date2:")
str3=str1[len(str1)-4:]
str4=str2[len(str2)-4:]
a=int(str3)
b=int(str4)
total1=0
total2=0
list1=[]
list2=[]
for i in range(a,b+1):
    if(i%100==0):
        if(i%400==0):
            total1=total1+1
            list1.append(i)
        else:
            total2=total2+1
            list2.append(i)
    else:
        if(i%4==0):
            total1=total1+1
            list1.append(i)
        else:
            total2=total2+1
            list2.append(i)
print("number of leap years:",total1)
print(list1)
print("number of non leap years:",total2)
print(list2)


