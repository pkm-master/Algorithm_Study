def dfs(tot) :
    global ans
    
    if tot >= ans :
        return

    if check() :
        if ans>tot :
            ans = tot
    
    else :
        for r in range(10):
            for c in range(10):
                if arr[r][c] == 0 :
                    continue
                for s in range(4,-1,-1):
                    if r+s >= 10 or c+s>=10:
                        continue
                    if result[s] >= 5:
                        continue
                    if not search(r,c,s):
                        continue
                    cover(r,c,s)
                    dfs(tot+1)
                    uncover(r,c,s)
                return 

def cover(i,j,s) :
    for r in range(i, i+s+1):
        for c in range(j, j+s+1):
            arr[r][c] = 0
    result[s] += 1

def uncover(i,j,s):
    for r in range(i, i+s+1):
        for c in range(j, j+s+1):
            arr[r][c] = 1
    result[s] -= 1

def search(i,j,s) : 
    for r in range(i,i+s+1):
        for c in range(j,j+s+1):
            if arr[r][c] == 0:
                return False 
    
    return True

def check():
    for r in range(10):
        for c in range(10):
            if arr[r][c]:
                return False
    return True

arr = [list(map(int,input().split())) for _ in range(10)]
ans = 25
result = [0]*5

dfs(0)

ans = ans if ans < 25 else -1 
print(ans)