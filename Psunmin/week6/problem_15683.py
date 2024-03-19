import copy
def d1(arr):
    dirs1=[(0,1)]
    for d in dirs1:
                ny=y+d[0]
                nx=y+d[1]
                if 0<=ny<Y and 0<=nx<X:
                    arr[ny][nx]="#"
                    ny+=d[0]
                    nx+=d[1]
                ny-=d[0]
                nx-=d[1]
                arr[ny][nx]=0
                if arr[ny][nx]==6:
                    break
    return arr
def d2(arr):
    dirs2=[(0,-1),(0,1)]
    for d in dirs2:
                ny=y+d[0]
                nx=y+d[1]
                if 0<=ny<Y and 0<=nx<X:
                    arr[ny][nx]="#"
                    ny+=d[0]
                    nx+=d[1]
                ny-=d[0]
                nx-=d[1]
                arr[ny][nx]=0
                if arr[ny][nx]==6:
                    break
    return arr

def d3(arr):
    dirs3=[(-1,0),(0,1)]
    for d in dirs3:
                ny=y+d[0]
                nx=y+d[1]
                if 0<=ny<Y and 0<=nx<X:
                    arr[ny][nx]="#"
                    ny+=d[0]
                    nx+=d[1]
                ny-=d[0]
                nx-=d[1]
                arr[ny][nx]=0
                if arr[ny][nx]==6:
                    break
    return arr
def d4(arr):
    dirs4=[(0,-1),(-1,0),(0,1)]
    for d in dirs4:
                ny=y+d[0]
                nx=y+d[1]
                if 0<=ny<Y and 0<=nx<X:
                    arr[ny][nx]="#"
                    ny+=d[0]
                    nx+=d[1]
                ny-=d[0]
                nx-=d[1]
                arr[ny][nx]=0
                if arr[ny][nx]==6:
                    break
    return arr
def d5(arr):
    dirs5=[(0,-1),(-1,0),(0,1),(1,0)]
    for d in dirs5:
                ny=y+d[0]
                nx=y+d[1]
                if 0<=ny<Y and 0<=nx<X:
                    arr[ny][nx]="#"
                    ny+=d[0]
                    nx+=d[1]
                ny-=d[0]
                nx-=d[1]
                arr[ny][nx]=0
                if arr[ny][nx]==6:
                    break
    return arr



Y,X=map(int,input().split())
arr=[list(map(int,input().split()))for i in range(Y)]

arr_90=[[0]*X for i in range (Y)]
arr_180=[[0]*X for i in range (Y)]
arr_270=[[0]*X for i in range (Y)]

for y in range (Y):
    for x in range (X):
        arr_90[y][x]=arr[Y-x-1][y]
        arr_180[y][x]=arr[Y-y-1][X-x-1]
        arr_270[y][x]=arr[x][Y-y-1]
        
        
for y in range (Y):
    for x in range (X):
        if arr[y][x]==1:
            copy_arr_0=copy.deepcopy(d1(copy_arr_0))
            copy_arr_90=copy.deepcopy(d1(copy_arr_90))
            copy_arr_180=copy.deepcopy(d1(copy_arr_180))
            copy_arr_270=copy.deepcopy(d1(copy_arr_270))
        elif arr[y][x]==2:
            copy_arr_0=copy.deepcopy(d2(copy_arr_0))
            copy_arr_90=copy.deepcopy(d2(copy_arr_90))
            copy_arr_180=copy.deepcopy(d2(copy_arr_180))
            copy_arr_270=copy.deepcopy(d2(copy_arr_270))
        elif arr[y][x]==3:
            copy_arr_0=copy.deepcopy(d3(copy_arr_0))
            copy_arr_90=copy.deepcopy(d3(copy_arr_90))
            copy_arr_180=copy.deepcopy(d3(copy_arr_180))
            copy_arr_270=copy.deepcopy(d3(copy_arr_270))
        elif arr[y][x]==4:
            copy_arr_0=copy.deepcopy(d4(copy_arr_0))
            copy_arr_90=copy.deepcopy(d4(copy_arr_90))
            copy_arr_180=copy.deepcopy(d4(copy_arr_180))
            copy_arr_270=copy.deepcopy(d4(copy_arr_270))
        elif arr[y][x]==5:
            copy_arr_0=copy.deepcopy(d5(copy_arr_0))
            copy_arr_90=copy.deepcopy(d5(copy_arr_90))
            copy_arr_180=copy.deepcopy(d5(copy_arr_180))
            copy_arr_270=copy.deepcopy(d5(copy_arr_270))