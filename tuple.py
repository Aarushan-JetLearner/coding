variable1=("red","orange","yellow","green","blue")
print(variable1[1])
for i in variable1:
    print(i)
#can't modify variable1[2]="black" It is immutable.
print(variable1[1:4])
r,o,y,g,b=variable1
print(r,o,y,g,b)
variable2=("string",["red","blue"],False,("green","yellow"))
print(variable2[1][1])
variable2[1][1]="white"
print(variable2[1][1])