# 다른 사람의 코드

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
cloud = [[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]]
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

move = []
for i in range(m) :
    temp = list(map(int, input().split()))
    move.append([temp[0] - 1, temp[1]])

for i in range(m) :
    # 1단계
    moving = move[i]
    next_cloud = []
    for c in cloud :
        x = c[0]
        y = c[1]
        d, s = moving[0], moving[1]
        nx = (n + x + dx[d] * s) % n
        ny = (n + y + dy[d] * s) % n
        next_cloud.append([nx, ny])

    # 2단계
    visited = [[False] * n for _ in range(n)]
    for drop in next_cloud :
        x = drop[0]
        y = drop[1]
        data[x][y] += 1
        visited[x][y] = True

    # 3단계
    cloud = []

    # 4단계
    cx = [-1, -1, 1, 1]
    cy = [-1, 1, -1, 1]
    for j in next_cloud :
        x = j[0]
        y = j[1]
        count = 0
        for k in range(4) :
            nx = x + cx[k]
            ny = y + cy[k]
            if 0 <= nx < n and 0 <= ny < n and data[nx][ny] >= 1 :
                count += 1
        data[x][y] += count

    # 5단계
    for j in range(n) :
        for k in range(n) :
            if data[j][k] >= 2 and visited[j][k] == False :
                data[j][k] -= 2
                cloud.append([j, k])


# 최종
result = 0
for i in range(n) :
    result += sum(data[i])

print(result)