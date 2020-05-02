x = int(input('Enter the number whose no. of digits is to be found out:'))
c=0
while x>0:
   x=x//10
   c=c+1
print('No. of digits in the number')
print(c)

