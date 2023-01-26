tc = int(input())
for k in range(tc):
    n, c = input().split()
    for i in range(len(c)):
        for j in range(int(n)):
            print(c[i], end='')


