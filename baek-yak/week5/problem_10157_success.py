# 10157 자리배정
    
n, m = map(int, input().split())
k = int(input())

if n*m < k:
    print(0)

else:
    di = [1,0,-1,0]
    dj = [0,1,0,-1]
    
    arr = [[1]*(n+2)]+[[1]+[0]*n+[1] for _ in range(m)]+[[1]*(n+2)]
    
    ci = 1
    cj = 1
    dr = 0
    
    for i in range(1,k):
        arr[ci][cj] = i
        ni = ci + di[dr]
        nj = cj + dj[dr]
        
        if arr[ni][nj] == 0:
            ci = ni
            cj = nj
        
        else:
            dr = (dr+1)%4
            ci = ci + di[dr]
            cj = cj + dj[dr]

    print(f'{cj} {ci}')       