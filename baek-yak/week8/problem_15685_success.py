# 15685 드래곤 커브

# 규칙 문제
# k 드래곤 커브는 k-1의 끝 점 기준으로 90 시계 방햐으로 회전 시킨 다음 붙인것
# 0 > 1 > 2, 1 > 2, 3, 2, 1

def drangon(dragon_curves):
    di = [1, 0, -1, 0]
    dj = [0, -1, 0, 1]

    arr = [[0] * 101 for _ in range(101)]

    for i, j, d, g in dragon_curves:
        arr[j][i] = 1
        temp = [d]
        
        # 이동방향
        q = [d]
        
        for _ in range(g + 1):
            for k in q:
                i += di[k] 
                j += dj[k]
                arr[j][i] = 1
            
            q = [(i + 1) % 4 for i in temp]
            q.reverse()
            
            temp = temp + q

    ans = 0
    
    for i in range(100):
        for j in range(100):
            if (arr[i][j] and arr[i][j + 1] and arr[i + 1][j] and arr[i + 1][j + 1]):
                ans += 1
                
    return ans


n = int(input())
dragon_curves = []

for _ in range(n):
    i, j, d, g = map(int, input().split())
    dragon_curves.append((i, j, d, g))

ans = drangon(dragon_curves)

print(ans)
