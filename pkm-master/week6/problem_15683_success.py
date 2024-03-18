def cctv(i,n) :
    global min_ans
    if i == n :
        new_visi = [visited[i][:] for i in range(len(visited))]
        for el in range(len(ls)) :
            st_i = ls[el][0]
            st_j = ls[el][1]
            st_dir = dir[ls[el][2]][:]

            for _ in range(path[el]) :
                st_dir = turn_90(st_dir)
                        
            for di in st_dir :
                new_st_i = st_i + di[0]
                new_st_j = st_j + di[1]

                while 0<=new_st_i<N and 0<=new_st_j<M and arr[new_st_i][new_st_j] !=6 :
                    
                    new_visi[new_st_i][new_st_j] = True
                    new_st_i += di[0]
                    new_st_j+= di[1]
        
        ans = sum([new_visi[j].count(False) for j in range(len(new_visi))])
        if ans < min_ans :
            min_ans = ans
    else :
        
        for j in range(4) :
            path[i] = j
            cctv(i+1,n)


dir = [[],[(0,1)],[(0,1),(0,-1)],[(-1,0),(0,1)],[(0,1),(-1,0),(0,-1)],[(0,1),(1,0),(0,-1),(-1,0)]]
def turn_90(ls) :
    for i in range(len(ls)) :
        if ls[i] == (0,1):
            ls[i] = (1,0)
        elif ls[i] == (1,0) :
            ls[i] = (0,-1)
        elif ls[i] == (0,-1) :
            ls[i] = (-1,0)
        else :
            ls[i] = (0,1)
    return ls

ls = []
N,M=map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
min_ans = 8*8
visited = [[False]*M for _ in range(N) ]
for i in range(N) :
    for j in range(M) :
        if 0<arr[i][j]<6:
            ls.append((i,j,arr[i][j]))
            visited[i][j]  = True
        if arr[i][j] == 6 :
            visited[i][j] = True

path = [0]*len(ls)
cctv(0,len(ls))
print(min_ans)