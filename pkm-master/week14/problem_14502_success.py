from collections import deque

def bfs():
    for p in path :
        arr[p[0]][p[1]] = 1
    
    q = deque()
    for virus in init_virus :
        q.append(virus)
    
    while q : 
        now = q.popleft()
        arr[now[0]][now[1]] = 2 
        
        for i in range(4) : 
            nr = now[0]+dr[i]
            nc = now[1]+dc[i]
            
            if 0<=nr<N and 0<=nc<M and arr[nr][nc] == 0 :
                q.append((nr,nc))

def count():
    blank = 0
    
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0 : 
                blank += 1
    return blank 

def rollback():
    for blank in init_blank : 
        arr[blank[0]][blank[1]] = 0

def dfs(i,j):
    global ans 
    if i == 3 :
        bfs()
        tmp = count()
        rollback()
        if ans < tmp :
            ans = tmp 
    else :
        for k in range(j,K) :
            path[i] = init_blank[k]
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
    for j in range(M):
        if arr[i][j] == 0 :
            init_blank.append((i,j))
        elif arr[i][j] == 1:
            init_wall.append((i,j))
        else :
            init_virus.append((i,j))

path = [(0,0)]*3
K = len(init_blank)

ans = 0
dfs(0,0)
print(ans)



