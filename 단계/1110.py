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