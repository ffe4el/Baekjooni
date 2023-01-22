a= list(map(int,input().split()))
li=[]

for i in range(1,a[0]):
    if a[i] > sum(a)/len(a) :
        li.append(a[i])
print(f"{((len(a)-1)/n*100):.3f}%")