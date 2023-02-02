# 11047 동전
import sys

input = sys.stdin.readline
n, k = map(int, input().split())
a=[]
cnt = 0

for _ in range(n):
    a.append(int(input()))

for i in range(n-1,-1,-1):
    if a[i] <= k:
        while(k >= a[i]):
            k = k - a[i]
            # print(a[i])
            cnt += 1

print(cnt)
