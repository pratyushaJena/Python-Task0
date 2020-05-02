str = input('Enter the string:')
i=0
print('The characters present at the even index are:')
l=len(str)
while i<l:
  if i%2==0:
    print(str[i])
  i=i+1


