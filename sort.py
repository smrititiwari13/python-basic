l = list(map(int, input("Enter list elements separated by space: ").split()))
n=len(l)
max=l[0]
min=l[n-1]
sum=0
for i in range(n):
  sum+=l[i]
  if(l[i]>max):
    max=l[i]
  if(l[i]<min):
    min=l[i]
  
    
print(max)
print(min)
print(sum)
l.sort()
print(l)
