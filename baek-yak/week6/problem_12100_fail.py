# 2048
'''
상 하 좌 우 각각 함수로 구현
테케는 맞았는데 틀렸다.
'''
from pprint import pprint

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def dfs(s, lst=[]):
    global ans
    if s == 5:
        ans = max(ans, play(lst))
        return
    for i in range(4):
        dfs(s+1, lst+[i])
    
def play(nums):
    copy_arr = [i[::] for i in arr]
    
    for num in nums:
        if num == 0:
            u(copy_arr)
        elif num == 1:
            d(copy_arr)
        elif num == 2:
            l(copy_arr)
        else:
            r(copy_arr)
    
    x = 0
    for i in copy_arr:
        x = max(x, max(i))
    
    return x

def u(copy_arr):
    for j in range(N):
        for i in range(N-1):
            if copy_arr[i][j] == 0:
                continue
                
            for k in range(i+1, N):
                if copy_arr[k][j] != 0:
                    if copy_arr[i][j] == copy_arr[k][j]:
                        copy_arr[i][j] *= 2
                        copy_arr[k][j] = 0
                        break
    
    for j in range(N):
        for i in range(N):
            if copy_arr[i][j] != 0:
                for k in range(i):
                    if copy_arr[k][j] == 0:
                        copy_arr[k][j] = copy_arr[i][j]
                        copy_arr[i][j] = 0
                    break
    for i in copy_arr:
        print(i)
    print('#') 
                
def d(copy_arr):
    for j in range(N):
        for i in range(N-1, 0, -1):
            if copy_arr[i][j] == 0:
                continue
                
            for k in range(i-1, -1, -1):
                if copy_arr[k][j] != 0:
                    if copy_arr[i][j] == copy_arr[k][j]:
                        copy_arr[i][j] *= 2
                        copy_arr[k][j] = 0
                    break
    
    for j in range(N):
        for i in range(N-1, -1, -1):
            if copy_arr[i][j] != 0:
                for k in range(N-1, i, -1):
                    if copy_arr[k][j] == 0:
                        copy_arr[k][j] = copy_arr[i][j]
                        copy_arr[i][j] = 0
                        break
    for i in copy_arr:
        print(i)
    print('#') 
    
def l(copy_arr):
    for i in range(N):
        for j in range(N-1):
            if copy_arr[i][j] == 0:
                continue
                
            for k in range(j+1, N):
                if copy_arr[i][k] != 0:
                    if copy_arr[i][j] == copy_arr[i][k]:
                        copy_arr[i][j] *= 2
                        copy_arr[i][k] = 0
                    break
    
    for i in range(N):
        for j in range(N):
            if copy_arr[i][j] != 0:
                for k in range(j):
                    if copy_arr[i][k] == 0:
                        copy_arr[i][k] = copy_arr[i][j]
                        copy_arr[i][j] = 0
                        break
    for i in copy_arr:
        print(i)
    print('#') 
                    
def r(copy_arr):
    for i in range(N):
        for j in range(N-1, 0, -1):
            if copy_arr[i][j] == 0:
                continue
                
            for k in range(j-1, -1, -1):
                if copy_arr[i][k] != 0:
                    if copy_arr[i][j] == copy_arr[i][k]:
                        copy_arr[i][j] *= 2
                        copy_arr[i][k] = 0
                    break
    
    for i in range(N):
        for j in range(N-1, -1, -1):
            if copy_arr[i][j] != 0:
                for k in range(N-1, j, -1):
                    if copy_arr[i][k] == 0:
                        copy_arr[i][k] = copy_arr[i][j]
                        copy_arr[i][j] = 0
                        break
    for i in copy_arr:
        print(i)
    print('#')   

ans = 0
dfs(0)
print(ans)