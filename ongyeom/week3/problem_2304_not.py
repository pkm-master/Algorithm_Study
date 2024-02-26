N = int(input())
C = [0]*1001
for _ in range(N):
    L, H = map(int, input().split())
    C[L] = H
...