list=[]
n=int(input("enter the no of colours:"))
for i in range(0,n):
    list.append(str(input()))
print(list)
print("the first colour",list[0])
print("the second colour",list[-1])
