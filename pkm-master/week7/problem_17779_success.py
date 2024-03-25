from collections import deque

N = int(input())
arr = [ list(map(int,input().split())) for _ in range(N)]
path_arr = [[0]*N for _ in range(N)]
total_min = int(1e9)

for x in range(N):
    for y in range(N) :
        for d1 in range(1,N-x) :
            for d2 in range(1,N-y+1) :
                total = deque([(i, j) for i in range(N) for j in range(N)])
                ans = [0]*5

                while total :
                    i,j = total.popleft()
                    if x<=i<=x+d1+d2 and y-d1<=j<=y+d2 and x-i+abs(y-j)<=0 and i-x+y-j<=2*d1 and i-x+j-y<=2*d2  :
                        ans[4]+=arr[i][j]
                        path_arr[i][j] = 5
                    elif  0<=i<x+d1 and 0<=j<=y and x-i+abs(y-j)>0 :
                        ans[0]+=arr[i][j]
                        path_arr[i][j] = 1
                    elif 0<=i<=x+d2 and y<j<=N-1 and x-i+abs(y-j)>0  :
                        ans[1]+=arr[i][j]
                        path_arr[i][j] = 2
                    elif x+d1 <=i<=N-1 and 0<=j<y-d1+d2 and i-x+y-j>2*d1 :
                        ans[2]+=arr[i][j]
                        path_arr[i][j] = 3
                    elif x+d2 < i <= N-1 and y-d1+d2<=j<=N-1 and i-x+j-y>2*d2:
                        ans[3]+=arr[i][j]
                        path_arr[i][j] = 4
                    else :
                        path_arr[i][j]=0
                if 0 not in ans :
                    part_min = max(ans)-min(ans)
                    if part_min<total_min :
                        total_min=part_min

print(total_min)