# find the elements present in k+n index
# k=3
# n=3
# [3,6,8,4,61,2]
# output:2
# ----------
# k=3
# n=4
# [80,70,54,36,72]
# output:error


my_list=list(map(int,input().split(" ")))
k=int(input())
n=int(input())
if(len(my_list)<k+1):
    print("error")
else:
    for i in range(0,len(my_list)):
        print(my_list[k+n],end=" ")  
        break