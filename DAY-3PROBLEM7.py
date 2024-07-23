# find the duplictes in an array
# [8,7,7,8,5,4,4,8,9]
# output:[8,7,4]

my_list=list(map(int,input().split(" ")))
new_list=[]
for i in my_list:
    if(i not in new_list):
        new_list.append(i)
print(new_list)        

