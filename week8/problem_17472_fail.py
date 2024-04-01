n, m = list(map(int, input().split()))
arr = [[0] * m for _ in range(n)]

for a in range(n):
    data = list(map(int, input().split()))
    for b in range(m):
        arr[a][b] = data[b]

dirs=[(0,1),(0,-1),(1,0),(-1,0)]