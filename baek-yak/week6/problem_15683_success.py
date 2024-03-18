# 15683 CCTV

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

d = {
    1 : [[0], [1], [2], [3]],
    2 : [[0,2], [1,3]],
    3 : [[0,1], [1,2], [2,3], [3,0]],
    4 : [[0,1,2], [1,2,3], [2,3,0], [3,0,1]],
    5 : [[0,1,2,3]]
}

def x():
    cctv = []
    ans = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 6 and arr[i][j] !=0:
                cctv.append((arr[i][j], i, j))
            if arr[i][j] == 0:
                ans += 1
    return cctv, ans

cctv, ans = x()

def move(i, j, dirs, copy):
    for dir in dirs:
        ni, nj = i, j
        
        while True:
            ni += di[dir]
            nj += dj[dir]
            
            if ni < 0 or ni >= N or nj < 0 or nj >= M or copy[ni][nj] == 6:
                break
            if copy[ni][nj] != 0:
                continue
            copy[ni][nj] = '!'

def zero(copy):
    global ans
    cnt = 0
    for i in copy:
        cnt += i.count(0)
    ans = min(ans, cnt)
    
def dfs(level, arr):
    copy_arr = [[j for j in arr[i]] for i in range(N)]
    
    if level == len(cctv):
        zero(copy_arr)
        return
    
    num, i, j = cctv[level]
    
    for ds in d[num]:
        move(i, j, ds, copy_arr)
        dfs(level + 1, copy_arr)
        copy_arr = [[j for j in arr[i]] for i in range(N)]
        

dfs(0, arr)
print(ans)