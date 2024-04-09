import copy

dir = [(0,-1),(1,0),(0,1),(-1,0)]


def rot(rat,di):
    for key,val in rat.items():
        new_val = []
        for ele in val :
            if di == (1,0):
                new_ele = (-ele[1],ele[0])
            elif di ==(0,1) :
                new_ele = (ele[0],-ele[1])
            else : 
                new_ele = (ele[1],ele[0])
            new_val.append(new_ele)
        rat[key] = new_val

    return rat

def add_sand(to,di,N):
    global sand
    r,c = to
    sands = A[r][c] 
    rat = rats[dir.index(di)]

    for val in rat : 
        for pos in rat[val] :
            if 0<=r+pos[0]<N and 0<=c+pos[1]<N :
                A[r+pos[0]][c+pos[1]] += int(sands*val)
            else : 
                sand += int(sands*val)
            A[r][c] -= int(sands*val)
    
    if 0<=r+di[0]<N and 0<=c+di[1]<N :
        A[r+di[0]][c+di[1]] += A[r][c]
    else : 
        sand+= A[r][c]
        
    A[r][c] = 0


N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]
rats = [{ 
        0.01 : [(-1,1),(1,1)],
        0.02 : [(-2,0),(2,0)],
        0.07 : [(-1,0),(1,0)],
        0.1: [(-1,-1),(1,-1)],
        0.05 : [(0,-2)]
    } for _ in range(4)]

for i,di in enumerate(dir):
    if di == (0,-1):
        continue
    
    rats[i] = rot(copy.deepcopy(rats[0]),di)


st = (N//2, N//2)
i=1
cnt=0
sand = 0

while st != (0,0):
    while i<=N:
        for di in dir :
            for _ in range(i):
                new_r = st[0]+di[0]
                new_c = st[1]+di[1]
                st = (new_r,new_c)
                add_sand(st,di,N)

                if st == (0,0): 
                    break
            else : 
                cnt+=1
                if cnt == 2:
                    i+=1 
                    cnt=0
                continue
            break
        else:
            continue
        break
    else:
        continue
    break
            

print(sand)