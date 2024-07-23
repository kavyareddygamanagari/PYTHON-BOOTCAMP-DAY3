#print the elemrnt in particular index in cyclic printing   IMP
# k=3
#[3 6 8 4 61 2]
#op:4
#------
#k=8
#[80 70 54 36 72]
#op:36

my_list=list(map(int,input().split(" ")))
k=int(input())
idx=k%len(my_list)
print(my_list[idx])
