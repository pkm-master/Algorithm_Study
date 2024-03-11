C,R = map(int,input().split())
visited = [[False]*R for _ in range(C)]
n = int(input())
dir = [(0,1),(1,0),(0,-1),(-1,0)]

if n == 1 :
    print(1, 1)
elif n > C*R :
    print('0')
else:
    cnt = 1
    st = (0,0)
    visited[0][0]=True
    while cnt < n:
        for di in dir :
            new_i = st[0]
            new_j = st[1]
            while 0<=new_i<C and 0<=new_j<R:
                new_i = st[0] + di[0]
                new_j = st[1] + di[1]
                if 0<=new_i<C and 0<=new_j<R and not visited[new_i][new_j]:
                    if cnt == n-1 :
                        print(new_i+1,new_j+1)
                    visited[new_i][new_j]=True
                    st = (new_i,new_j)
                    cnt+=1
                else:
                    break
