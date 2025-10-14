set1={"Hello!",0,False,1,2,3}
print(set1)
length=len(set1)
print(length)
set1.add(5)
print(set1)
for i in set1:
    print(i)
set1.remove(1)
print(set1)
if 5 in set1:
    print("It's in set1")
set1.pop()
print(set1)
#set1.clear()
print(set1)
set2={"Bye!",3,True,1,7,8}
print(set2)
variable1=set1|(set2)
print(variable1)
variable2=set1&(set2)
print(variable2)
set1.update(set2)
print(set1)
variable3=set1.symmetric_difference(set2)
print(variable3)
set1.symmetric_difference_update(set2)
print(set1)
#set1[1]=10
