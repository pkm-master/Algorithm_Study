X,Y=map(int,input().split())
N=int(input())
arr=[[0]*X for i in range(Y)]

dirs=[(-1,0),(0,1),(1,0),(0,-1)]

num=0
ny=Y
nx=0
while 1:
    for d in dirs:
        ny+= d[0]
        nx+=d[1]
        while 0<=ny<Y and 0<=nx<X and arr[ny][nx]==0:
            num+=1
            arr[ny][nx]=num
            ny += d[0]
            nx += d[1]
        ny-=d[0]
        nx-=d[1]
    if num==X*Y:
        break
# print(arr)
flag=False
for y in range(Y):
    for x in range(X):
        if arr[y][x]==N:
            print(x+1,Y-y)
            flag=True
            break
if flag==False:
    print(0)