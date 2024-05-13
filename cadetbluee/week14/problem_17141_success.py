from collections import deque
from itertools import combinations

dr = [0,1,0,-1]
dc = [1,0,-1,0]
N,M = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(N)]


wall = []

virus_sub = []

for r in range(N) :
    for c in range(N) :
        if grid[r][c] == 1 :
            wall.append((r,c))
    
        elif grid[r][c] == 2 :
            virus_sub.append((r,c))
            grid[r][c] = 0

res = 10e9

for virus in combinations(virus_sub,M) :

    visited = [[0]*N for _ in range(N)]

    v = deque(virus[:])

    for r,c in virus :
        grid[r][c] = 2 
        visited[r][c] = 1

    cnt = M+len(wall)
    while v :
        cr,cc = v.popleft()

        for d in range(4) :
            nr = cr + dr[d]
            nc = cc + dc[d]

            if 0<=nr<N and 0<=nc<N and not visited[nr][nc] and grid[nr][nc] == 0 :
                visited[nr][nc] = visited[cr][cc] + 1 
                v.append((nr,nc))
                cnt += 1 
      
            if N**2 - cnt == 0:
                tmp = 0
                for r in range(N) :
                    tmp = max(max(visited[r]),tmp)
                
                if tmp<res :
                    res = tmp 
                break

    for r,c in virus :
        grid[r][c] = 0

if res>=10e9 :
    print(-1)
else :
    print(res-1)