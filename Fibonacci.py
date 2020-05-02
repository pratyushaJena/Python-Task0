x = int(input('Enter the number of terms of the series:'))
print('The fibonacci series:')
if(x==0|x==1):
    print('1')
if x<0:
    print('Fibonacci series does not exist')
if x>0:
  a=0
  b=1
  print(a)
  print(b)
  for i in range(2,x):
      c=a+b
      print(c)
      a=b
      b=c


n=int(input('Enter the number to be checked for fibonacci number'))
d=0
e=1
if n==0|n==1:
    print('It is a fibonacci number')
if n<0:
    print('It is not a fibonacci number')
while n>0:
    f=d+e
    if(f==n):
        print('It is a fibonacci number')
        break
    if(f>n):
        print('it is not a fibonacci number')
        break
    d=e
    e=f

