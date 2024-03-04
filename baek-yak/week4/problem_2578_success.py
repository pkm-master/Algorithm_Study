# 2578 빙고
arr = [list(map(int, input().split())) for _ in range(5)]
mc = [list(map(int, input().split())) for _ in range(5)]

cnt = 0

def c(x):
    ans = 0
    for i in range(5):
        if sum(x[i]) == 0:
            ans += 1
    
    for i in range(5):
        sub = 0
        for j in range(5):
            if x[j][i] == 0:
                sub += 1
        if sub == 5:
            ans +=1
    
    d1 = []
    d2 = []
    
    for i in range(5):
        d1.append(x[i][i])
        d2.append(x[i][4-i])
        
    if sum(d1) == 0:
        ans += 1
    
    if sum(d2) == 0:
        ans += 1
        
    return ans

for i in range(5):
    for j in range(5):
        
        for k in range(5):
            for l in range(5):
                if mc[i][j] == arr[k][l]:
                    arr[k][l] = 0
                    cnt += 1
                
                    if c(arr) >= 3:
                        print(cnt)
                        exit()

