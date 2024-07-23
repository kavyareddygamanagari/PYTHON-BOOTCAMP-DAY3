# replace the elements in an array with average of max and min elements
# test case:0
# [13 2 67 20 68]
# 68+2=70==35
#[35 35 35 35 35]

my_list=list(map(int,input().split(" ")))
maxi=my_list[0]
mini=my_list[0]
for i in range(0,len(my_list)):
    if(my_list[i]>maxi):
        maxi=my_list[i]
for j in range(0,len(my_list)):
    if(my_list[j]<mini):
        mini=my_list[j]
        avg=((maxi+mini)/2)  
for i in range(0,len(my_list)):     
        my_list[i]=avg
print(my_list)          