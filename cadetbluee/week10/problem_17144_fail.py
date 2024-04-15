from pprint import pprint
R,C,T=map(int,input().split())
arr=[list(map(int,input().split()))for _ in range(R)]
for i in range(R):
    if arr[i][0]==-1:
        puri=[i,i+1]
        break
fd=[(-1,0),(0,1),(1,0),(0,-1)]
sd=[(1,0),(0,1),(-1,0),(0,-1)]
amount=[[0]*C for _ in range(R)]

for _ in range(T):

    for r in range(R):
        for c in range(C):
            if arr[r][c]>0:
                amount[r][c]=arr[r][c]//5
    for r in range(R):
        for c in range(C):
            if arr[r][c]>0:
                temp=amount[r][c]
                for d in [(0,1),(0,-1),(-1,0),(1,0)]:
                    nr=r+d[0]
                    nc=c+d[1]
       
                    if 0<=nr<R and 0<=nc<C and arr[nr][nc]>=0:
                        arr[nr][nc]+=temp
                        arr[r][c]-=temp

    temp=0
    cur=[puri[0],0]
    while True:
        r,c=cur[0],cur[1]
        nr=r+fd[temp][0]
        nc=c+fd[temp][1]
        
        if  temp>2 and nr==puri[0] and nc==0:
            break
        if 0<=nr<=puri[0] and 0<=nc<C:
            cur=[nr,nc]
            arr[r][c],arr[nr][nc]=arr[nr][nc],arr[r][c]
 
        else:
            temp+=1
    arr[puri[0]][0]=-1
    arr[puri[0]][1]=0
    temp=0
    cur=[puri[1],0]
    while True:
        r,c=cur[0],cur[1]
        nr=r+sd[temp][0]
        nc=c+sd[temp][1]
    
        if temp>2 and nr==puri[1] and nc==0 :
            break
        if puri[1]<=nr<R and 0<=nc<C:
            cur=[nr,nc]
            arr[r][c],arr[nr][nc]=arr[nr][nc],arr[r][c]
        else:
            temp+=1
    arr[puri[1]][0]=-1
    arr[puri[1]][1]=0

result=0
for a in arr:
    for i in a:
        if i !=-1:
            result+=i
            
print(result)