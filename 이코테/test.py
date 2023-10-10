n,m = map(int, input().split())

arr = [[0] * m] * n

for i in range(n):
    arr[i] = int(input())

for i in range(n):
    for j in range(m):
        print(arr[i][j])
    print("\n")