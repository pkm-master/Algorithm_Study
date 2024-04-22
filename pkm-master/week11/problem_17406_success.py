from copy import deepcopy

def rotate(r,c,s,rotated_arr):
    if s == 0 :
        return 
    else : 
        start = rotated_arr[r-s][c-s]
        for i in range(r-s,r+s) :
            rotated_arr[i][c-s] = rotated_arr[i+1][c-s]
        for j in range(c-s,c+s) : 
            rotated_arr[r+s][j] = rotated_arr[r+s][j+1]
        for i in range(r+s,r-s,-1):
            rotated_arr[i][c+s] = rotated_arr[i-1][c+s]
        for j in range(c+s,c-s,-1):
            rotated_arr[r-s][j] = rotated_arr[r-s][j-1]
        rotated_arr[r-s][c-s+1] = start

        rotate(r,c,s-1,rotated_arr)

def find_min(i,k):
    global min_val
    if i == k:
        rotated_arr = deepcopy(arr)
        for el in path : 
            rotate(*rotations[el],rotated_arr)
            
        for r in range(N) :
            sum_r = sum(rotated_arr[r])
            if sum_r < min_val :
                min_val = sum_r

        
    else : 
        for j in range(k):
            if j not in path[:i]:
                path[i] = j 
                find_min(i+1,k)
                path[i] = -1 
            

N,M,K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
rotations = [(0,0,0)]*K
for i in range(K):
    r,c,s = map(int,input().split())
    rotations[i] = (r-1,c-1,s)

min_val = 100*50
path = [-1]*K
find_min(0,K)

print(min_val)