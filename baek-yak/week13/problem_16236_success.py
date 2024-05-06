'''
백준 16236 아기 상어

아기상어(크기 2) 상하좌우 한칸 이동, 작거나 같은 경우만 이동
먹는 조건 
작은 경우, 가장 가까운 경우. 먹을때마다 크기 1 증가
더 이상 먹을 수 없는 시간 출력
'''
from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1 ,1]

def bfs(si, sj):
    q = deque()
    v = [[0]*N for _ in range(N)]
    eat = []

    q.append((si, sj))
    v[si][sj]=1
    eatting = 0

    while q:
        # q에서 데이터 꺼냄
        ci, cj = q.popleft()     

        if eatting == v[ci][cj]:
            return eat, eatting-1

        # 이동
        for d in range(4):
            ni = ci + di[d] 
            nj = cj + dj[d]
            
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and shark >= arr[ni][nj]:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj]+1
                
                if shark > arr[ni][nj] > 0:
                    eat.append((ni, nj))
                    eatting = v[ni][nj]
    return eat, eatting-1

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        # 아기상어
        if arr[i][j] == 9:
            ci, cj = i, j
            arr[i][j]=0

shark = 2
cnt = 0
ans = 0

while True:
    eat, dist = bfs(ci,cj)
    
    # 먹을 물고기 없는 경우
    if len(eat)==0:
        break
    
    eat.sort(key=lambda x: (x[0],x[1]))
    ci, cj = eat[0]
    
    # 물고기 먹기
    arr[ci][cj]=0           
    cnt += 1
    
    ans += dist
    
    # 크기만큼 물고기 먹은경우 크기+1
    if shark == cnt:          
        shark += 1
        cnt = 0
        
print(ans)