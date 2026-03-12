n=int(input('Enter a number'))
if n>1:
    for i in range(2,n//2+1):
        if n%i==0:
            print('Number is not a prime')
            break
    else:
        print('Number is prime')
else:
    print('Number is not a prime')

