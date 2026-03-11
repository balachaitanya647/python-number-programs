n=int(input())
dummy=n
l=len(str(n))
s=0
while dummy>0:
    rem=dummy%10
    dummy=dummy//10
    s+=rem**l
if s==n:
    print('Given Number is Armstrong Number')
else:
    print('Given Number is Not Armstrong Number')
    
