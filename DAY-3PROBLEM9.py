# find the sum of squares of a digit at a given number

n=1234
sum=0
while n>0:
    r=n%10
    sum=sum+r*r
    n=n//10
print(sum)    
