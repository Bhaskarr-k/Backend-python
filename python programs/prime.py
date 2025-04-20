n=3
t=0
if n<=1:
    t=1
for j in range(2,n):
    if n%j==0:
        t=1
        break
    if t==0:
        print('prime')
    else:
        print('not prime')
