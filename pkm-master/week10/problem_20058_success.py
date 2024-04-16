from collections import deque

def rotation(part) : 
    n = len(part)
    new_arr = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_arr[i][j] = part[n-j-1][i]
    return new_arr 

def tornado(L):
    global arr
    if L == N :
        arr = rotation(arr)
    
    elif L == 0:
        pass
    
    else :
        for r in range((2**N)//(2**L)):
            for c in range((2**N)//(2**L)):
                part = [ [ arr[i][j] for j in range(2**L*c-1*((2**L*c)%2),2**L*(c+1))]  for i in range(2**L*r-1*((2**L*r)%2),2**L*(r+1))]
                new_part = rotation(part)
                for i in range(2**L):
                    for j in range(2**L):
                        arr[2**L*r+i][2**L*c+j] = new_part[i][j]


def meltdown():
    melt_ls = deque() 
    for i in range(2**N):
        for j in range(2**N):
            if arr[i][j] > 0 :
                cnt = 0
                for di in dir:
                    new_i = i+di[0]
                    new_j = j+di[1]
                    if 0<=new_i<2**N and 0<=new_j<2**N and arr[new_i][new_j]>0:
                        cnt +=1

                if cnt < 3 :
                    melt_ls.append((i,j))
    
    while melt_ls :
        i,j = melt_ls.popleft()
        arr[i][j]-=1

def sum_ice() :
    s = 0
    for i in range(2**N):
        for j in range(2**N):
            s+=arr[i][j]
            if arr[i][j] == 0:
                visited[i][j] = 1
    return s 

def check_big():
    big = 1
    for i in range(2**N):
        for j in range(2**N):
            if visited[i][j] == 1 :
                continue
            else :
                q = deque()
                q.append((i,j))
                cnt = 0
                while q :
                    r,c = q.popleft()
                    if visited[r][c] == 1 :
                        continue
                    visited[r][c] = 1
                    cnt +=1
                    for di in dir :
                        new_r = r + di[0]
                        new_c = c + di[1]
                        if 0<=new_r<2**N and 0<=new_c<2**N and not visited[new_r][new_c]:
                            q.append((new_r,new_c))

                if big < cnt :
                    big = cnt
                    
    if big == 1:
        return 0
    return big 

N,K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(2**N)]
Ls = list(map(int,input().split()))
dir = [(-1,0),(1,0),(0,-1),(0,1)]
visited = [[False]*(2**N) for _ in range(2**N)]

for L in Ls :
    tornado(L)
    meltdown()
    
s = sum_ice()
b = check_big()

print(s)
print(b)
