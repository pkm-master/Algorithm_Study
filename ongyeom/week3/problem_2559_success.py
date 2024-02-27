N, K = map(int, input().split())
T = list(map(int, input().split()))
max_add = sum(T[0:K])
add = 0
for i in range(N):
    add += T[i]
    if i < K-1:
        continue
    elif i == K-1:
        pass
    else:
        add -= T[i-K]
    if max_add < add:
        max_add = add
print(max_add)
