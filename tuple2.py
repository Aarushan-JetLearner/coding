details_all_groups=[]
for i in range(5):
    onedata_recorder1=input("Please enter the group name")
    twodata_recorder1=input("Please enter the group size")
    threedata_recorder1=input("Please enter the venue")
    fourdata_recorder1=input("Please enter the medal type")
    variable=(onedata_recorder1,twodata_recorder1,threedata_recorder1,fourdata_recorder1)
    details_all_groups.append(variable)
for i in details_all_groups:
    print(i)


