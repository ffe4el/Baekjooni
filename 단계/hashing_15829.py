#아니 솔직히 뭔소리인지 잘 모르겠음;;;

r = 31
M = 1234567891
n = int(input())
word = input()
hashh = 0

for i in range(n):
    alpha = ord(word[i]) -96
    hashh += alpha*(r**i)

print(hashh%M)
