# 게임 개발
n, m = map(int, input().split())  # 맵 크기
a, b, c = map(int, input().split())  # 현재 캐릭터의 위치(a,b)와 바라보고 있는 방향(c)

li = [[0 for col in range(m)] for row in range(n)]
cmp = [[0 for col in range(m)] for row in range(n)]

for i in range(n):  # 배열에 저장 성공
    li[i] = list(map(int, input().split()))  # 0이 육지, 1이 바다

for i in range(n):
    for j in range(m):
        cmp[i][j] = 1  # 1로 초기화


def game(row, col, c, result):
    if c == 0:  # 북
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        dc = [3, 2, 1, 0]
    elif c == 1:  # 동
        dx = [0, -1, 0, 1]
        dy = [-1, 0, 1, 0]
        dc = [0, 3, 2, 1]
    elif c == 2:  # 남
        dx = [1, 0, -1, 0]
        dy = [0, -1, 0, 1]
        dc = [1, 0, 3, 2]
    elif c == 3:  # 서
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        dc = [2, 1, 0, 3]

    cnt = 0  # 4면 모두 못갈때
    for i in range(4):
        ny = row + dy[i]
        nx = col + dx[i]
        nc = dc[i]

        if li[ny][nx] == 0 and cmp[ny][nx] == 1:  # 해당하는 곳이 육지이고 한번도 지나간적이 없다면
            cmp[ny][nx] = 0  # 지나갔다는 표시
            result += 1
            game(ny, nx, nc, result)
        elif li[ny][nx] == 1 or cmp[ny][nx] == 0:
            cnt += 1
            game(row, col, nc, result)

    if cnt == 4:
        for i in range(4):
            if dc[i] == nc:
                last = i
                break
        if dy[last] != 0:
            ny = row - dy[i]  # 뒤로가기
            nx = col
            if li[ny][nx] == 1:
                return result
            game(ny, nx, nc, result)
        elif dx[last] != 0:
            ny = row
            nx = col - dx[i]  # 뒤로가기

            if li[ny][nx] == 1:
                return result
            game(ny, nx, nc, result)


game(a, b, c, 0)
