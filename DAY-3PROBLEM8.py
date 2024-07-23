# sum of digits
# n=1+2+3+3+4+2=15

n=123342
sum=0
while n>0:
    r=n%10
    sum=sum+r
    n=n//10
print(sum)
