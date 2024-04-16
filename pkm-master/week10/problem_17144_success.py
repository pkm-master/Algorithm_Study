from collections import deque

dir = [(0,1),(1,0),(0,-1),(-1,0)]

def init():
    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0:
                munjis.append([i,j,arr[i][j]])


def count():
    s = 0
    for i in range(R):
        for j in range(C):
            if arr[i][j] != -1:
                s+=arr[i][j]
    
    return s

def diffusion():
    while munjis : 
        munji = munjis.popleft()
        if munji[2] < 5 :
            continue
        else :
            diffuse = munji[2]//5
            for di in dir :
                new_r = munji[0]+di[0]
                new_c = munji[1]+di[1]
                if 0<=new_r<R and 0<=new_c<C and arr[new_r][new_c] != -1:
                    arr[new_r][new_c] += diffuse 
                    arr[munji[0]][munji[1]] -= diffuse


def clean():
    upper = air_fresher[0][0]
    for i in range(upper-1,0,-1):
        arr[i][0] = arr[i-1][0]
    for j in range(C-1):
        arr[0][j] = arr[0][j+1]
    for i in range(upper):
        arr[i][C-1] = arr[i+1][C-1]
    for j in range(C-1,1,-1):
        arr[upper][j] = arr[upper][j-1]
    arr[upper][1] = 0
    
    lower = air_fresher[1][0]
    for i in range(lower+1,R-1):
        arr[i][0] = arr[i+1][0]
    for j in range(C-1):
        arr[R-1][j] = arr[R-1][j+1]
    for i in range(R-1,lower,-1):
        arr[i][C-1] = arr[i-1][C-1]
    for j in range(C-1,1,-1):
        arr[lower][j] = arr[lower][j-1]
    arr[lower][1] = 0
    

R,C,T = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(R)]
air_fresher = []

for i in range(R):
    if arr[i][0] == -1:
        air_fresher.append((i,0))
        air_fresher.append((i+1,0))
        break

for _ in range(T):
    munjis = deque()
    init()
    diffusion()
    clean()
    
s = count()
print(s)
