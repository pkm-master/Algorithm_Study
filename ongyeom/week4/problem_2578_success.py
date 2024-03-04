def bingo():
    sc = 0
    cr = 0
    cl = 0
    for i in range(5):
        ci = 0
        cj = 0
        for j in range(5):
            if arr[i][j] == 0:
                ci += 1
            if arr[j][i] == 0:
                cj += 1
        if ci == 5: sc += 1
        if sc == 3: return sc
        if cj == 5: sc += 1
        if sc == 3: return sc
        if arr[i][i] == 0:
            cr += 1
        if arr[i][4-i] == 0:
            cl += 1
    if cr == 5: sc += 1
    if sc == 3: return sc
    if cl == 5: sc += 1
    if sc == 3: return sc

arr = [list(map(int, input().split())) for _ in range(5)]
c = 0
mc = []
for _ in range(5):
    mc += list(map(int, input().split()))
while 1:
    n = mc.pop(0)
    for x in range(5):
        if n in arr[x]:
            y = arr[x].index(n)
            arr[x][y] = 0
            c += 1
    if bingo() == 3:
        break
print(c)