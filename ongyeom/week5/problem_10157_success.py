def where(arr):
    for i in range(len(arr)):
        if who in arr[i]:
            y = arr[i].index(who)
            x = i
            return f'{y + 1} {len(arr) - x}'

def snail():
    global x, y
    arr = [[0]*y for _ in range(x)]
    cnt = 1
    ci, cj = x, 0
    ii, jj = -1, 1
    y -= 1
    while cnt <= max_xy:
        for i in range(x):
            ci = ci + ii
            arr[ci][cj] = cnt
            cnt+=1
            if cnt >= max_xy:
                break
        else:
            x -= 1

        for j in range(y):
            cj = cj + jj
            arr[ci][cj] = cnt
            cnt+=1
            if cnt >= max_xy:
                break
        else:
            y -= 1
        ii *= (-1)
        jj *= (-1)
    return where(arr)

def position():
    if who > max_xy:
        return 0
    else:
        return snail()

y, x = map(int, input().split())
who = int(input())
max_xy = x*y
print(position())