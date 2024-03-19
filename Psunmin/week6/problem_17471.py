def recur(x,N):
    if x==N:
        print(popular)
        return
    
    for i in range(x,N):
        popular[x],popular[i]=popular[i],popular[x]
        recur(x+1,N)
        popular[x],popular[i]=popular[i],popular[x]

N=int(input())
arr= [0]+list(map(int,input().split()))
popular=[]
for i in range(N+1):
    popular.append([i,arr[i]])
graph={}
    
for i in range(1,N+1):
    lst=list(map(int,input().split()))
    n=lst[0]
    graph[i]=lst[1:]

print(popular)
recur(1,N+1)
        