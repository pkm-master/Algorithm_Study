import sys
sys.stdin = open('input.txt')

N,M = map(int,input().split())
r,c,d = map(int,input().split())
cnt = 1
arr = [list(map(int,input().split())) for _ in range(N)]
dir = [(-1,0),(0,1),(1,0),(0,-1)]
    
arr[r][c] = 2
    
while 0<=r<N and 0<=c<M : 
    for _ in range(4):
        d=(d+3)%4
        new_r = r+dir[d][0]
        new_c = c+dir[d][1]
        
        if 0<=new_r<N and 0<=new_c<M and arr[new_r][new_c]==0:
            r = new_r
            c = new_c
            arr[r][c]=2
            cnt+=1
            break
    else : 
        new_r = r-dir[d][0]
        new_c = c-dir[d][1]
        if new_r>=N or new_c>=M or new_r<0 or new_c<0 : 
            break
        if arr[new_r][new_c]==1 : 
            break
        r = new_r
        c = new_c

print(cnt)