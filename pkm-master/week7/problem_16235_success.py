import sys
sys.stdin = open('input.txt')

from pprint import pprint
N,M,K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
tree = [ [[] for _ in range(N)] for _ in range(N)]
ground = [[5]*N for _ in range(N)]
dir = [(0,1),(0,-1),(1,-1),(1,1),(-1,1),(-1,-1),(-1,0),(1,0)]

for i in range(M) : 
    x,y,z = map(int,input().split())
    tree[x-1][y-1].append(z)

while K > 0 :
    for i in range(N) :
        for j in range(N): 
            tree[i][j].sort()
            live_tree = []
            additional = 0
            
            for el in tree[i][j]:
                if ground[i][j]-el < 0 :
                    additional += el//2
                else : 
                    ground[i][j] -= el
                    live_tree.append(el+1)
            
            tree[i][j] = live_tree
            ground[i][j] += additional

    for i in range(N) :
        for j in range(N):
            for el in tree[i][j] :
                if el %5==0:
                    for di in dir :
                        new_r = i + di[0]
                        new_c = j + di[1]
                        if 0<=new_r<N and 0<=new_c<N :            
                            tree[new_r][new_c].append(1)
            
            ground[i][j] += arr[i][j]

    K-=1

cnt = 0
for i in range(N) : 
    for j in range(N) : 
        cnt+=len(tree[i][j])

print(cnt)


