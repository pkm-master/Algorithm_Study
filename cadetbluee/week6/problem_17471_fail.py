
def bfs(g):
    q = []
    check = [0 for _ in range(n)]
    q.append(g[0])
    check[g[0]] = 1
    cnt, ans = 1, 0
    while q:
        x = q.popleft()
        ans += people[x]
        for nx in a[x]:
            if nx in g and not check[nx]:
                check[nx] = 1
                cnt += 1
                q.append(nx)
    if cnt == len(g):
        return ans
    else:
        return 0

n = int(input())
people = list(map(int, input().split()))

a = [[] for _ in range(n)]
for i in range(n):
    x = list(map(int, input().split()))
    for j in range(1, x[0]+1):
        a[i]

