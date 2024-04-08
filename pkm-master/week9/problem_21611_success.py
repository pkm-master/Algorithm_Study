dir = [(-1,0),(1,0),(0,-1),(0,1)] 
index = {}

def indexing():
    r,c = N//2, N//2
    di = 0
    H = 1
    i = 1
    
    tmpA = [[0]*N for _ in range(N)]
    snail = [(0,-1),(1,0),(0,1),(-1,0)]
    cnt=0
    while 0<=r<N and 0<=c<N:
        tmpA[r][c]=i        
        index[i]=(r,c)   
        r+=snail[di][0]
        c+=snail[di][1]        
        cnt+=1        
        if cnt==H: 
            if di == 1 or di==3:
                H+=1 
            di=(di+1)%4 
            cnt=0
        i+=1

def bliz(d,s):
    st_r,st_c = N//2, N//2
    for i in range(s):
        new_r = st_r+dir[d-1][0]*(i+1)
        new_c = st_c+dir[d-1][1]*(i+1)
        if A[new_r][new_c]:
            A[new_r][new_c]=0    

def move(): 
    st = 2 
    end = 3 
    while st < N**2 and end <= N**2 :
        while st < N**2:
            st_r,st_c = index[st]
            if not A[st_r][st_c]:
                break
            st+=1
        else:
            return
        
        if end <= st:
            end = st+1
            
        while end<=N**2 :
            end_r,end_c = index[end]
            if A[end_r][end_c]: 
                break
            end+=1
        else:
            return 
        
        A[st_r][st_c]=A[end_r][end_c]
        A[end_r][end_c]=0            

def destory(): 
    global check
    check = False
    st = 2
    end = 3
    cnt = 1  
    while st<N**2 and end<=N**2:
        st_r,st_c = index[st]
        end_r,end_c = index[end]
        if A[st_r][st_c] == A[end_r][end_c]: 
            cnt+=1
            end+=1
        else: 
            if cnt>=4: 
                check = True   
                for i in range(st,end):
                    now_r,now_c = index[i]
                    marb[A[now_r][now_c]-1]+=1 
                    A[now_r][now_c]=0 
            cnt=1
            st=end
            end+=1

def change(): 
    newA = [[0]*N for _ in range(N)]
    st = 2
    end = 3
    i = 2
    cnt = 1    

    while st < N**2 and end<=N**2:
        st_r,st_c = index[st]
        end_r,end_c = index[end]
        
        if A[st_r][st_c] == A[end_r][end_c]: 
            cnt+=1
            end+=1
            
        else:
            r,c = index[i]
            newA[r][c] = cnt   
            r,c = index[i+1]
            newA[r][c] = A[st_r][st_c] 
            i+=2            
            cnt=1
            st=end
            end+=1

        if i>N**2:
            break
        
    for i in range(N):
        for j in range(N):
            A[i][j] = newA[i][j]

N,M = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
blis = [list(map(int,input().split())) for _ in range(M)]
marb = [0,0,0] 

indexing() 
for bli in blis:
    d,s = bli
    bliz(d,s)
    move()
    check = True
    while check :
        destory()
        move()
    change()
print(marb[0]+marb[1]*2+marb[2]*3)

