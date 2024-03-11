arr=[[0]*1001 for _ in range (1001)]
n=int(input())

for i in range (n):
    x,y,w,h=map(int,input().split())
    
    for p in range(y,y+h):
        for q in range(x,x+w):
            arr[p][q]=i+1

for i in range(n):
    sum=0
    for p in range(1001):
        for q in range(1001):
            if arr[p][q]==i+1:
                sum+=1
    # for k in arr:
    #     for j in k:
    #         if j==i:
    #             sum+=1
    print(sum)