n = input()
m = int(n)
i = 0

if 0 < int(n) < 10:
    n = "0" + n
elif int(n)==0:
    print("1")

while True:
    if int(n)==0:
        break
    a = int(n[0])+int(n[1])
    b = str(a)
    if a>9:
        n= n[1]+b[1]
    else :
        n=n[1]+b
    i= i+1
    if int(n) == m :
        break

if int(n) != 0:
    print(i)