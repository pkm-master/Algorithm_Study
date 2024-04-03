Y,X=map(int,input().split())
pos=list(map(int,input().split()))
dirs=[(-1,0),(0,1),(1,0),(0,-1)]

arr=list(map(int,input().split()))

# for y in range(Y):
#     for x in range(X):
y,x,d=pos
while y<Y:
    while x<X:
        if arr[y][x]==0: arr[y][x]=1
        