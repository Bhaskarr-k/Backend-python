n=153
p=len(str(n))
r=0
for x in str(n):
    c=int(x)
    r=r+c**p
if n==r:
    print('arm strong number')
else:
    print('not arm strong number')
