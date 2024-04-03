
from pprint import pprint

# 점을 기준으로 점을 90도 돌리고 extends해준 것을 return
def dr_cur(dc) : 
    new = []

    end = dc[-1] 
    arr[end[1]][end[0]] = 1
    for i in range(len(dc)-2,-1,-1):
        delta_x = dc[i][0] - end[0]
        delta_y = dc[i][1] - end[1]
        new_x = end[0] - delta_y
        new_y = end[1] + delta_x
        if 0<=new_x<=100 and 0<=new_y<=100:
            new.append((new_x,new_y))
            if arr[new_y][new_x] != 1 :
                arr[new_y][new_x] = 1
    
    dc.extend(new)
    return dc

arr = [[0]*101 for _ in range(101)]
dir = [(1,0),(0,-1),(-1,0),(0,1)]

N = int(input())
for _ in range(N):
    x,y,d,g = map(int,input().split())
    
    end = (x+dir[d][0],y+dir[d][1])
    dc = [(x,y), end]
    arr[y][x]=1
    arr[end[1]][end[0]]=1
    
    for _ in range(g):
        dc = dr_cur(dc)

cnt=0
for i in range(100):
    for j in range(100):
        if arr[i][j]==1 and arr[i+1][j]==1 and arr[i][j+1]==1 and arr[i+1][j+1]==1:
            cnt+=1

print(cnt)