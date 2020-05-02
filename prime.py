sI = int(input('Enter the starting interval:'))
eI = int(input('Enter the ending interval:'))
c=0
print('prime numbers in the given range')

for i in range(sI,eI+1):
    for j in range(1,i+1):
        if i%j==0:
            c=c+1
    if c==2:
        print(i)
    c=0

n=int(input('Enter the number to be checked for prime number:'))
p=0
for k in range(1,n+1):
    if n%k==0:
            p=p+1
if p==2:
   print('Entered number is prime')
else:
   print('Entered number is not prime')


