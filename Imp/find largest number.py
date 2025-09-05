#find largest number in list 
# bubble sort

l = [21,400,63,22,65,32,90]
n = len(l)

for i in range(n):
    for j in range(0,n-i-1):
        if l[j]<l[j+1]:
            l[j], l[j+1]=l[j+1],l[j]
    print(l)
    
            
print(l[0])
