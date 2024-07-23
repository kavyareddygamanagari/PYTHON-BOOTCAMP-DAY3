# find the reverse number in a digit at a given number
# ****important****

n=1234
rev=" "
while n>0:
    r=n%10
    rev=rev+str(r)
    n=n//10
print(int(rev))  