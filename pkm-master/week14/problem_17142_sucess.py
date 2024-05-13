from pprint import pprint

from collections import deque

def bfs(blank):
    global ans
    visited = [[0]*N for _ in range(N)]
    q = deque()
    time = 0
    
    for p in path :
        q.append((p[0],p[1]))
        visited[p[0]][p[1]] = 1
        arr[p[0]][p[1]] = 3
        
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1 :
                visited[i][j] = 1

    is_fill = False
    while q : 
        if blank == 0 :
            is_fill = True
            break
        
        now = q.popleft()
        
        for i in range(4) : 
            nr = now[0]+dr[i]
            nc = now[1]+dc[i]
            
            if 0<=nr<N and 0<=nc<N and visited[nr][nc] == 0 :
                q.append((nr,nc))
                visited[nr][nc] = visited[now[0]][now[1]] + 1
                if arr[nr][nc] == 0 :
                    blank -= 1

        if arr[now[0]][now[1]] == 2 :
            visited[now[0]][now[1]] -= 1

    if is_fill : 
        time = 0
        for i in range(N):
            for j in range(N):
                if visited[i][j] > time :
                    time = visited[i][j]

        return time
    else : 
        return False

def rollback():
    for virus in init_virus : 
        arr[virus[0]][virus[1]] = 2

def dfs(i,j,blank):
    global ans 
    if i == M :
        tmp = bfs(blank)
        if tmp and ans > tmp :
            ans = tmp
        rollback()
    else :
        for k in range(j,K) :
            path[i] = init_virus[k]
            dfs(i+1,k+1,blank)
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
        elif arr[i][j] == 0 :
            init_blank.append((i,j))
        else :
            init_virus.append((i,j))

path = [(0,0)]*M
K = len(init_virus)
blank = len(init_blank)

ans = 50*50
dfs(0,0,blank)

if ans == 50*50 :
    print(-1)
else :
    print(ans-1)



