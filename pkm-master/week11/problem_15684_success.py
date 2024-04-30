from copy import deepcopy

def add_ladder(i,n,idx):
    global ans
    if ans != -1 :
        return 
    
    if i == n :

        if check():
            ans = n 

    else:
        for x in range(idx,N):
            for y in range(1,H+1):
                if y not in ladders[x] and y not in ladders[x+1] and y not in ladders[x-1] :
                    ladders[x].add(y)
                    add_ladder(i+1,n,x)
                    ladders[x].remove(y)
        

def check():
    global cnt 
    cnt+=1
    
    for i in range(1,N+1):
        c = i
        r = 0

        while r <= H :
            if r in ladders[c] :
                c+=1
                r+=1
            elif r in ladders[c-1] :
                c-=1 
                r+=1
            else : 
                r+=1

        if c != i :
            return False
    else :
        return True


N,M,H = map(int,input().split())
right = [set() for _ in range(N+1)]
ans = -1
cnt = 0
all_ladders = set()

for m in range(M):
    a,b = map(int,input().split())
    right[b].add(a)

for i in range(4):
    ladders = deepcopy(right)
    add_ladder(0,i,1)
    if ans != -1 :
        break 


print(ans)
