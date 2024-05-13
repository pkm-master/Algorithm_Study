'''
백준 17142 연구소3

바이러스 비활성
활성 바이러스는 인접칸으로 복제(1초)
M개 활성 상태로 변경

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

def bfs(tlst):
    q = deque()
    v = [[0]*N for _ in range(N)]

    for ti,tj in tlst:
        q.append((ti,tj))
        v[ti][tj]=1

    cnt = CNT

    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0),(1, 0),(0, -1),(0, 1)):
            ni = ci + di
            nj = cj + dj
            
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and arr[ni][nj] != 1:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1

                # 빈칸
                if arr[ni][nj] == 0:      
                    cnt -= 1
                    # 모든 빈칸 채운경우
                    if cnt == 0:
                        return v[ni][nj] - 1

    return N*N

def dfs(n, s, tlst):
    global ans

    if n == M:
        ans = min(ans, bfs(tlst))
        return

    for j in range(s, VCNT):
        dfs(n+1, j+1, tlst+[vlst[j]])

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 빈칸 개수
CNT = 0
vlst = []

for i in range(N):
    for j in range(N):
        
        # 빈 칸
        if arr[i][j] == 0:    
            CNT += 1
        # 비활성 바이러스
        elif arr[i][j] == 2:  
            vlst.append((i, j))

VCNT = len(vlst)

# 처음부터 빈칸 없음 => 0
if CNT==0:                  
    ans = 0
else:
    ans = N*N
    dfs(0, 0, [])
    
    # 빈칸 남아있는 경우
    if ans == N*N:
        ans = -1
print(ans)