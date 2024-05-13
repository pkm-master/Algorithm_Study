'''
백준 17141 연구소2

바이러스 M개, 승원이의 신호와 퍼지기 시작

연구소는 N * N, 벽은 한 칸을 차지
빈 칸은 바이러스를 놓을 수 있으며 인접한 칸으로 동시에 복제(1초)
모든 빈 칸에 바이러스가 퍼지는 최소 시간

입력
연구소 크기 N, 바이러스 개수 M
연구소 상태(0 : 빈칸, 1 : 벽, 2 : 빈칸)

출력
모든 칸 바이러스 최소시간(불가능 -1)


'''
from collections import deque

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def bfs():
    global q, visit, ans
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + di[i]
            ny = y + dj[i]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == -1:
                if a[nx][ny] == 0:
                    visit[nx][ny] = visit[x][y] + 1
                    cnt = max(cnt, visit[nx][ny])
                    q.append([nx, ny])

    for i in range(n):
        for j in range(n):
            if a[i][j] == 0 and visit[i][j] == -1:
                cnt = float('inf')
    ans = min(ans, cnt)

def dfs(index, cnt):
    global q, visit, ans
    if cnt == m:
        q = deque()
        visit = [[-1]*n for _ in range(n)]
        for i in range(len(virus)):
            if select[i]:
                q.append([virus[i][0], virus[i][1]])
                visit[virus[i][0]][virus[i][1]] = 0
        bfs()
        return

    for i in range(index, len(virus)):
        if select[i]:
            continue
        select[i] = 1
        dfs(i+1, cnt+1)
        select[i] = 0

# 데이터 input
n, m = map(int, input().split())

a = []
virus = []

for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)
    for j in range(n):
        if a[i][j] == 2:
            virus.append([i, j])
            a[i][j] = 0

# 바이러스 최대 개수가 10이므로 range(10)
select = [0 for _ in range(10)]
visit = [[0]*n for _ in range(n)]

ans = float('inf')

q = deque()

dfs(0, 0)

if ans == float('inf'):
    print(-1)
else:
    print(ans)