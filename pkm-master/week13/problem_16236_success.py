from collections import deque
from heapq import heappop,heappush

dr = [-1,0,0,1]
dc = [0,-1,1,0]

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

sl = (0,0)
s = 2
fl = []
ans = 0
cnt = 0

for i in range(N):
    for j in range(N):
        if arr[i][j]==9:
            sl=(i,j)
            arr[i][j] = 0
        else :
            fl.append((i,j))
            

def bfs(start):
    q = deque()
    q.append(start)
    visited = [[0]*N for _ in range(N)]
    visited[start[0]][start[1]] = 1
    candidate = []
    
    while q :
        curr = q.popleft()

        for i in range(4):
            new_r = curr[0] + dr[i]
            new_c = curr[1] + dc[i]

            
            if 0<=new_r<N and 0<=new_c<N and 0<arr[new_r][new_c]<s:
                heappush(candidate,(visited[curr[0]][curr[1]] ,new_r,new_c))
            
            elif 0<=new_r<N and 0<=new_c<N and arr[new_r][new_c]<=s and visited[new_r][new_c] == 0:
                visited[new_r][new_c] = visited[curr[0]][curr[1]] + 1
                q.append((new_r,new_c))
                
    if candidate :
        return heappop(candidate)
    
new_sl = bfs(sl)

while new_sl :
    arr[new_sl[1]][new_sl[2]] = 0

    ans += new_sl[0]
    cnt += 1
    
    if s == cnt :
        s +=1
        cnt = 0 

    sl = (new_sl[1],new_sl[2])
    new_sl = bfs(sl)
    
print(ans)
