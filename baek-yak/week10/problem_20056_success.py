'''
마법사 상어와 파이어볼
'''
N,M,K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

di = [-1,-1,0,1,1,1,0,-1]
dj = [0,1,1,1,0,-1,-1,-1]

for _ in range(K):
    # 0 = i, 1 = j, 2 = 질량, 3 = 속도, 4 = 방향
    # 이동
    for i in range(len(arr)):
        arr[i][0] = (arr[i][0] + di[arr[i][4]] * arr[i][3]) % N + 1
        arr[i][1] = (arr[i][1] + dj[arr[i][4]] * arr[i][3]) % N + 1

    # 정렬(좌표기준 정렬 > 같은좌표 처리)
    arr.sort(key = lambda x : (x[0], x[1]))
    arr.append([100, 100, 0, 0, 0])
    new=[]

    # 같은좌표 합치고, 나누고 > new에 추가
    i=0
    while i < len(arr)-1:
        # 기준좌표
        si, sj, m, s, d = arr[i]
        start = 0
        for j in range(i+1, len(arr)):
            #  같은좌표
            if (si, sj) == (arr[j][0], arr[j][1]):  
                m += arr[j][2]
                s += arr[j][3]
                # 다른방향 start=1
                if d % 2 != arr[j][4] % 2:  
                    start=1
            # 다른좌표
            else:
                # 1개 > 추가
                if j-i==1:
                    new.append(arr[i])
                # 여러 개
                else:
                    # 나눠도 1이상(파이어볼 존재)
                    if m // 5 > 0:
                        for dr in range(start, start+8, 2):
                            new.append([si, sj, m//5, s//(j-i), dr])
                break
        i = j
    arr = new

ans = 0

for i in arr:
    ans += i[2]
    
print(ans)