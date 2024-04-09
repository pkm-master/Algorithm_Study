from collections import deque

dir = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
check_dir = [(-1,-1),(-1,1),(1,1),(1,-1)]

N,M = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
clouds = deque([(N-1,0),(N-1,1),(N-2,0),(N-2,1)])

for t in range(M) : 
    d,s = map(int,input().split())
    d=d-1

    for _ in range(len(clouds)):
        cloud = clouds.popleft()
        new_r = cloud[0]+dir[d][0]*s
        new_c = cloud[1]+dir[d][1]*s

        if new_r>=N :
            new_r = new_r%N
        if new_c>=N :
            new_c = new_c%N
        
        if new_r<0 :
            if new_r<=-N:
                new_r = -new_r%N
                if new_r != 0:
                    new_r = N-new_r
            else : 
                new_r = N+new_r

        if new_c<0 :
            if new_c<=-N:
                new_c = -new_c%N
                if new_c != 0:
                    new_c = N-new_c
            else : 
                new_c = N+new_c

        A[new_r][new_c] +=1
        clouds.append((new_r,new_c))
    
    clouds=set(clouds)
    for cloud in clouds : 
        tmp=0
        for di in check_dir :
            check_r = cloud[0] + di[0]
            check_c = cloud[1] + di[1]
            if 0<=check_r<N and 0<=check_c<N and A[check_r][check_c]>=1:
                tmp +=1
        A[cloud[0]][cloud[1]]+=tmp

    new_clouds=deque()
    for i in range(N):
        for j in range(N) :             
            if (i,j) not in clouds and A[i][j]>=2:
                A[i][j]-=2
                new_clouds.append((i,j))
                
    clouds = new_clouds
    
ans = 0
for i in range(N):
    for j in range(N):
        ans+=A[i][j]

print(ans)
        
        

