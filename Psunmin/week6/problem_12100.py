import copy
def left(arr):
    '''
    2 2 2  >  4 2 0
    4 4 4     8 4 0
    8 8 8     16 8 0
    '''
    for col in arr:
        # 2 0 0 2 -> 2 2 0 0 으로 바꿔주기
        # 숫자는 왼쪽으로 몰고, 빈 자리는 다시 0으로 채워주기
        O=col.count(0)
        col=list(filter(lambda x:x !=0, col))
        # arr=[x for x in col if x!=0]  둘다 0을 한번에 없애는 법
        col+=[0]*O
        
        # 앞뒤 숫자 같으면 더하고, 하나는 0으로 다시 바꿔주기
        for i in range (N-1):
            if col[i]==col[i+1]:
                col[i]=col[i]*2
                col[i+1]=0
    return arr

def right(arr):
    for col in arr:
        # 2 0 0 2 -> 2 2 0 0 으로 바꿔주기
        # 숫자는 왼쪽으로 몰고, 빈 자리는 다시 0으로 채워주기
        O=col.count(0)
        col=list(filter(lambda x:x !=0, col))
        # arr=[x for x in col if x!=0]  둘다 0을 한번에 없애는 법
        col=[0]*O+col
        
        # 앞뒤 숫자 같으면 더하고, 하나는 0으로 다시 바꿔주기
        for i in range (N-1,1,-1):
            if col[i]==col[i-1]:
                col[i]=col[i]*2
                col[i-1]=0
    return arr

def up(arr):
    row_arr=list(map(list,zip(*arr)))   # 편할려고 가로,세로 바꾸기
    for row in row_arr:
        O=row.count(0)
        row=list(filter(lambda x:x !=0, row))
        row=[0]*O+row
        # 앞뒤 숫자 같으면 더하고, 하나는 0으로 다시 바꿔주기
        for i in range (N-1):
            if row[i]==row[i+1]:
                row[i]=row[i]*2
                row[i+1]=0
def down(arr):
    row_arr=list(map(list,zip(*arr)))   # 편할려고 가로,세로 바꾸기
    for row in row_arr:
        O=row.count(0)
        row=list(filter(lambda x:x !=0, row))
        row=[0]*O+row
        # 앞뒤 숫자 같으면 더하고, 하나는 0으로 다시 바꿔주기
        for i in range (N-1,1,-1):
            if row[i]==row[i-1]:
                row[i]=row[i]*2
                row[i-1]=0
            
def result(n,arr):
    global ans
    if n==5:
        for i in range(N):
            for j in range(N):
                if arr[i][j]>ans:
                    ans=arr[i][j]
        return
   
    for i in range(4):
        copy_arr=copy.deepcopy(arr)
        if i==0:
            result(n+1,left(copy_arr))
        elif i==1:
            result(n+1,right(copy_arr))
        elif i==2:
            result(n+1,right(copy_arr))
        else:
            result(n+1,right(copy_arr))
        
N= int(input())
ans=0
arr=[list(map(int,input().split())) for i in range (N)]
result(0,arr)
print(ans)