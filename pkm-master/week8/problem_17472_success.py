from collections import deque
from heapq import heappop,heappush

dir = [(0,1),(0,-1),(1,0),(-1,0)]
INF = int(1e9)
N,M = map(int,input().split())
# 각 섬이 포함하는 좌표를 담는 dict를 만든다.
n = 0
visited = [[0]*M for _ in range(N)]
arr = [list(map(int,input().split())) for _ in range(N)]
isls = {}

for i in range(N):
    for j in range(M):
        if not visited[i][j] and arr[i][j] == 1 : 
            isls.setdefault(n,[(i,j)])
            # 주의를 돌면서 dict에 추가
            q = deque()
            q.append((i,j))
            visited[i][j]=1
            while q :
                st = q.pop()
                for di in dir :
                    new_i = st[0]+di[0]
                    new_j = st[1]+di[1]
                    if 0<=new_i<N and 0<=new_j<M and not visited[new_i][new_j] and arr[new_i][new_j]==1:
                        visited[new_i][new_j]=1
                        q.append((new_i,new_j))
                        isls[n].append((new_i,new_j))
            n+=1

adj = [set() for _ in range(n)]

for i in range(n):
    for gr1 in isls[i] : 
        for di in dir :
            br = 0
            new_i = gr1[0] + di[0]
            new_j = gr1[1] + di[1]
            while 0<=new_i<N and 0<=new_j<M and arr[new_i][new_j] != 1 :
                new_i +=di[0]
                new_j +=di[1]
                br+=1
            isl = None
            for key,value in isls.items() : 
                if (new_i,new_j) in value and br >=2 :
                    isl = key
            
            if isl is not None and isl!=i :
                adj[i].add((br,isl))

# 이제 이 정보들을 이용해 prim algorithm을 사용 
# 큐에 일단 0을 집어넣고 작은거를 선택해나아간다.

if set() in adj :
    ans = -1
    
else : 
    vis_isl = [0]*n
    h = []
    heappush(h,(0,0))
    ans = 0

    while h : 
        brd,now = heappop(h)
        if vis_isl[now] :
            continue
        vis_isl[now] = 1
        ans += brd

        for to in adj[now]:
            if vis_isl[to[1]] == 1 :
                continue 
            heappush(h,to)

    if 0 in vis_isl:
        ans = -1

print(ans)