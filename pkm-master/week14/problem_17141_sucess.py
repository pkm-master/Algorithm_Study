from collections import deque

def bfs():
    q = deque()

    for p in path :
        arr[p[0]][p[1]] = 1
        q.append((p[0],p[1]))
    
    while q : 
        now = q.popleft()
        
        for i in range(4) : 
            nr = now[0]+dr[i]
            nc = now[1]+dc[i]
            
            if 0<=nr<N and 0<=nc<N and arr[nr][nc] == 0 :
                q.append((nr,nc))
                arr[nr][nc] = arr[now[0]][now[1]] + 1

def is_fill():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0 :
                return False
    return True

def total_time():
    time = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > time :
                time = arr[i][j]
    return time

def rollback():
    for blank in init_blank : 
        arr[blank[0]][blank[1]] = 0

def dfs(i,j):
    global ans 
    if i == M :
        bfs()
        if is_fill() :
            tmp = total_time()
            if ans > tmp :
                ans = tmp
        rollback()

    else :
        for k in range(j,K) :
            path[i] = init_virus[k]
            dfs(i+1,k+1)
            path[i] = (0,0)

dr = [-1,1,0,0]
dc = [0,0,-1,1]
N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

init_virus = []
init_wall = []
init_blank = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            init_wall.append((i,j))
            arr[i][j] = -1
        else :
            init_blank.append((i,j))
            if arr[i][j] == 2 :
                init_virus.append((i,j))
                arr[i][j] = 0

path = [(0,0)]*M
K = len(init_virus)

ans = 50*50
dfs(0,0)

if ans == 50*50 :
    print(-1)
else :
    print(ans-1)



