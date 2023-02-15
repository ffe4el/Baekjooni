
def bin_search(a, key):
    left = 0
    right = len(a)-1

    while True:
        mid = (left+right)//2
        if a[mid] == key:
            return mid
        elif a[mid] > key:
            right = mid-1
        elif a[mid] < key:
            left = mid+1

        if left > right:
            break
    return -1

if __name__ == "__main__":
    num = int(input("원소의 수를 입력하세요. : "))
    x = [0]*num

    print('배열데이터를 오름차순으로 입력하세요. : ')

    x[0] = int(input('x[0] : '))

    for i in range(1, num):
        while True:
            x[i]=int(input(f"x[{i}] : "))
            if x[i] >= x[i-1]:
                break

    key = int(input("검색할 값을 입력하세요. : "))

    idx = bin_search(x, key)

    if idx==-1:
        print("검색값이 존재하지 않습니다.")
    else :
        print(f"검색값은 {idx}에 있습니다.")