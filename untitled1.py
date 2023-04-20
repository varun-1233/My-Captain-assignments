i= int(input('Enter limit '))
a=1
b=-1
c=0
while i>= 0:
  c=a+b
  b=a
  a=c
  print(c)
  i=i-1
