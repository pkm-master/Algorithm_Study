def bfs(i,n):
    global ans 
    if i == N//2:
        start_score = 0
        link_score = 0
        link_path = total_path.difference(path)
        
        for r in path:
            for c in path :
                start_score += score[r-1][c-1]
        
        for r in link_path:
            for c in link_path:
                link_score += score[r-1][c-1]
        
        if ans > abs(link_score-start_score):
            ans = abs(link_score-start_score)
                
    
    else:
        for j in range(n,N+1):
            if j not in path :
                path.add(j)
                bfs(i+1,j+1)
                path.remove(j)

N = int(input())
path = set()
total_path = set()
for i in range(N):
    total_path.add(i+1)
    
score = [list(map(int,input().split())) for _ in range(N)]

ans = 20*100
bfs(0,1)

print(ans)