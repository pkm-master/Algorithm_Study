# 10163 색종이 넓이 구하기

n = int(input())

arr = [[0]*1001 for _ in range(1001)]

for num in range(1, 1+n):
    x, y, w, h = map(int,input().split())
    
    for i in range(x,x+w):
        for j in range(y,y+h):
            arr[i][j] = num


for num in range(1, n+1):
    cnt = 0
    
    for i in arr:
        cnt += i.count(num)
        
    print(cnt)