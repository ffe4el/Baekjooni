# 10989 수 정렬3 이건 1억까지... 시간초과가 문제일것 같은데..

import sys

input = sys.stdin.readline

a = []
for _ in range(int(input())):
    a.append(int(input()))

a.sort()
for s in a:
    print(s)
