arr=[list(map(int,input().split())) for i in range (5)] #빙고판
num=[list(map(int,input().split())) for i in range (5)] #숫자 부르기
num=sum(num,[])  #이차배열을 1차로 변경

#빙고인지 검사
def check(arr):
    bingo=0
    for i in range(5):
        #행탐색
        if sum(arr[i])==0:  
            bingo+=1
        #열탐색
        col_sum=0
        for j in range(5):
            col_sum+=arr[j][i]
        if col_sum==0:
            bingo+=1
        # 열탐색 리스트컴프리헨션으로 변경하면 아래처럼
        # if sum([arr[j][i] for j in range(5)])==0:
        #     bingo+=1
        
    if sum(arr[i][i] for i in range(5))==0:
        bingo+=1
    if sum(arr[5-1-i][i] for i in range(5))==0:
        bingo+=1
    return bingo

flag=False        
for i in num:
    if flag:
        break
    for y in range(5):
        if flag:
            break
        for x in range(5):
            if arr[y][x]==i:
                arr[y][x]=0
                if check(arr)>=3:
                    print(num.index(i)+1)
                    flag=True
                    break