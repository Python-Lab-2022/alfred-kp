list1=[1,2,3,4,5,6,7,8]
list2=[11,13,2,15,5,6]
if len(list1)==len(list2):
    print("the list are of same length")
else:
    print("length are not same")
sum1=0
sum2=0
for i in list1:
    sum1=sum1+i
for i in list2:
    sum2=sum2+i
if sum1==sum2:
    print("lists sum are the same")
else:
    print("lists sum are not same")
z=int(input("enter the value to be checked:"))
if z in list1:
    print("the value is present in list1")
else:
    print("value not present in list1")
if z in list2:
    print("the value present i n list2")
else:
    print("value not present in list2")
