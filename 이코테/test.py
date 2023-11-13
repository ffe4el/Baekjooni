def binary_search(arr, target, start, end):
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid+1, end)
    else :
        return binary_search(arr, target, start, mid-1)


n = int(input())
a = list(map(int, input().split()))
a.sort() #사전 정렬

m = int(input())
b = list(map(int, input().split()))
b.sort() #사전 정렬

for i in range(len(b)):
    if binary_search(a, b[i], 0, len(a)-1):
        print("yes", end=' ')
    else :
        print("no", end=' ')

