string=str(input("enter the string:"))
print("the string is",string)
start=string[0]
end=string[-1]
res=end+string[1:-1]+start
print("the result is:",res)
