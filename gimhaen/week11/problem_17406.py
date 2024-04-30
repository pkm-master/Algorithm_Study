'''
5 6 2
1 2 3 2 5 6
3 8 7 2 1 3
8 2 3 1 4 5
3 4 5 1 1 1
9 3 2 1 4 3
3 4 2
4 2 1
'''

n, m, k = map(int, input().split())
origin_arr = [list(map(int, input().split())) for _ in range(n)]
new_arr = [[0]*m for _ in range(n)]
rcs = []
answer = []
for _ in range(k):
    r, c, s = map(int, input().split())
    rcs.append([r,c,s])

def rotation(r, c, s, arr):
    new_arr = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            new_arr[i][j] = arr[i][j]
 
    for shell in range(1, s+1):
        for x in range(2*shell):
            new_arr[r-1-shell][c-1-shell+1+x] = arr[r-1-shell][c-1-shell+x]
 
        for x in range(2*shell):
            new_arr[r-1-shell+1+x][c-1+shell] = arr[r-1-shell+x][c-1+shell]
 
        for x in range(2*shell):
            new_arr[r-1+shell][c-1+shell-1-x] = arr[r-1+shell][c-1+shell-x]
 
        for x in range(2*shell):
            new_arr[r-1+shell-1-x][c-1-shell] = arr[r-1+shell-x][c-1-shell]
 
    return new_arr
 
 
def sequence(index, k, table):
    global answer
    if index == k:
        r = rcs[table[0]][0]
        c = rcs[table[0]][1]
        s = rcs[table[0]][2]
        next_arr = rotation(r, c, s, origin_arr)
 
        for __ in range(1, k):
            r = rcs[table[__]][0]
            c = rcs[table[__]][1]
            s = rcs[table[__]][2]
            next_arr = rotation(r, c, s, next_arr)
 
        result = sum(next_arr[0])
        for idx in range(1, n):
            if result > sum(next_arr[idx]):
                result = sum(next_arr[idx])
 
        answer.append(result)
        return
 
    for _ in range(k):
        if _ in table:
            continue
        table.append(_)
        sequence(index+1, k, table)
        table.remove(_)
 
 
sequence(0, k, [])
 
print(min(answer))