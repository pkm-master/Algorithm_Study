# 17471 게리맨더링

def bfs(g, a, human, n):
    q = []
    check = [0 for _ in range(n)]
    q.append(g[0])
    check[g[0]] = 1
    cnt = 1
    ans = 0
    
    while q:
        x = q.pop(0)
        ans += human[x]
        for nx in a[x]:
            if nx in g and not check[nx]:
                check[nx] = 1
                cnt += 1
                q.append(nx)
    
    if cnt == len(g):
        return ans
    else:
        return 0

def dfs(cnt, x, end, c, n, a, human):
    global min_ans
    
    if cnt == end:
        g1 = []
        g2 = []
        
        for i in range(n):
            if c[i]:
                g1.append(i)
            else:
                g2.append(i)
        ans1 = bfs(g1, a, human, n)
        
        if not ans1:
            return
        ans2 = bfs(g2, a, human, n)
        
        if not ans2:
            return
        min_ans = min(min_ans, abs(ans2 - ans1))
        return
    
    for i in range(x, n):
        if c[i]:
            continue
        c[i] = 1
        dfs(cnt+1, i, end, c, n, a, human)
        c[i] = 0
        
n = int(input())
human = list(map(int, input().split()))

a = [[] for _ in range(n)]

for i in range(n):
    x = list(map(int, input().split()))
    for j in range(1, x[0]+1):
        a[i].append(x[j]-1)
        
min_ans = 99999

for i in range(1, n//2 + 1):
    c = [0 for _ in range(n)]   
    dfs(0, 0, i, c, n, a, human)
    
if min_ans == 99999:
    print(-1)
else:
    print(min_ans)