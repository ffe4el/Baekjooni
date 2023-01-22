<<<<<<< HEAD
a= list(map(int,input().split()))
li=[]

for i in range(1,a[0]):
    if a[i] > sum(a)/len(a) :
        li.append(a[i])
print(f"{((len(a)-1)/n*100):.3f}%")
=======
# 3052

n = [input() in range(10)]
n=[]
m=[]

for i in range(10):
    # int(input())
    k = int(n[i]) % 10
    if k not in m:
        m.append(k)

# print(m)
print(len(m))
>>>>>>> f0dce50520b4e0955a68c470a77626645f1e6902
