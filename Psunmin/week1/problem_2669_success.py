arr=[[0]*100 for _ in range (100)]     # 평면 만들기

for _ in range (4):                    # 네개의 직사각형 입력 받기
    x1,y1,x2,y2 = map(int,input().split())
    
    for y in range (y1,y2):
        for x in range (x1,x2):
            arr[y][x]=1                # 직사각형 범위 1로 변경
        
cnt=0
# 칠해진 넓이 구하는 방법1
for i in range (100):
    for j in range (100):
        if arr[i][j]==1:              # 칠해진 넓이 구하기
            cnt+=1
            
# 칠해진 넓이 구하는 방법2
# for i in arr:
#     cnt+=sum(i)

print(cnt)