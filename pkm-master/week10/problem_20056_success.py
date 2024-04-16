dirs = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

from collections import deque

def calibration(val) :
    if val>=N : 
        return val%N 
    elif 0<=val<N :
        return val
    elif -N<=val<0 : 
        return N+val 
    else :
        return val%N 

def move():
    while fireballs :
        fireball = fireballs.popleft()
        di = fireball[4]
        arr[fireball[0]][fireball[1]].popleft()
        
        fireball[0] += dirs[di][0] * fireball[3]
        fireball[1] += dirs[di][1] * fireball[3]
        fireball[0] = calibration(fireball[0])
        fireball[1] = calibration(fireball[1])
        arr[fireball[0]][fireball[1]].append((fireball[2],fireball[3],fireball[4]))

def combination(ls):
    total_M = 0
    total_S = 0
    di_counter = ls[0][2]%2
    total_di = True
    
    for el in ls :
        total_M += el[0]
        total_S += el[1]
        if di_counter != el[2]%2:
            total_di = False 

    each_M = total_M//5
    each_S = total_S//len(ls)
    
    if each_M == 0 :
        ls = deque([])
    else :
        if total_di :
            ls = deque([(each_M,each_S,0),(each_M,each_S,2),(each_M,each_S,4),(each_M,each_S,6)])
            for el in ls :
                fireballs.append([i,j,el[0],el[1],el[2]])
        else :
            ls = deque([(each_M,each_S,1),(each_M,each_S,3),(each_M,each_S,5),(each_M,each_S,7)])
            for el in ls :
                fireballs.append([i,j,el[0],el[1],el[2]])

    return ls

N,M,K = map(int,input().split())
arr = [[deque() for _ in range(N)] for _ in range(N)]
fireballs = deque()

for _ in range(M) : 
    r,c,m,s,d = map(int,input().split())
    fireballs.append([r-1,c-1,m,s,d])
    arr[r-1][c-1].append((m,s,d))

for _ in range(K):

    move()
    
    for i in range(N):
        for j in range(N):
            if len(arr[i][j]) == 1 :
                fireballs.append([i,j,arr[i][j][0][0],arr[i][j][0][1],arr[i][j][0][2]])
            if len(arr[i][j])>=2 :
                arr[i][j] = combination(arr[i][j])

s = 0
for i in range(N):
    for j in range(N):
        for el in arr[i][j]:
            s += el[0]

print(s)