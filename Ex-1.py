def isPrime(n):
    #Check the number greater than 1
    if n<=1:
        return False
    #check prime number
    for i in range(2,n):
        if n%i==0:
            return False
        else:
            return True
        
#Read an integer
pn = int(input('enter the integer number between 2 to 32767:'))
#Check the primenumber and print 
if isPrime(pn)==True:
    print('this number is prime number')
else:
    print('this number is not prime number')