'''
백준 14502 연구소

n x m 연구소
바이러스 인접카능로 퍼져나감
세울 수 있는 벽 3개 반드시 세워야 함
바이러스가 퍼질 수 없는 곳이 안전 영역
안전 영역의 최댓값을 구하기
'''
from collections import deque

def bfs(list):
    # 벽 막기
    for i, j in list:
        arr[i][j]=1

    q = deque()
    visit = [[0]*M for _ in range(N)]
    cnt = CNT - 3 

    for ti, tj in virus:
        q.append((ti, tj))
        visit[ti][tj]=1

    while q:
        ci, cj = q.popleft()

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni = ci + di 
            nj = cj + dj
            
            if 0 <= ni < N and 0 <= nj < M and visit[ni][nj] == 0 and arr[ni][nj] == 0:
                q.append((ni, nj))
                visit[ni][nj]=1
                cnt-=1

    #  벽 해체
    for i,j in list:
        arr[i][j]=0
    return cnt      


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 빈칸 위치, 바이러스 위치
lst = []
virus = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            lst.append((i, j))
        elif arr[i][j] == 2:
            virus.append((i, j))

CNT = len(lst)
v = [0]*CNT
ans = 0

for i in range(CNT-2):
    for j in range(i + 1, CNT - 1):
        for k in range(j + 1, CNT):
            ans = max(ans, bfs([lst[i], lst[j], lst[k]]))
            
print(ans)