# 다른 사람의 코드

delta = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def rotate_90(proportion):
    new_proportion = list(reversed(list(zip(*proportion))))
    return new_proportion

p = [[0, 0, 0.02, 0, 0], [0, 0.1, 0.07, 0.01, 0], [0.05, 0, 0, 0, 0], [0, 0.1, 0.07, 0.01, 0], [0, 0, 0.02, 0, 0]]
p1 = rotate_90(p)
p2 = rotate_90(p1)
p3 = rotate_90(p2)
proportions = [p, p1, p2, p3]
alphas = [(2, 1), (3, 2), (2, 3), (1, 2)] # 이해가 안 가는 부분

def solution():
    outer_sand = 0 
    tr = sr 
    tc = sc
    curl = 0  
    turn = 2  # 이해 안 가는 부분 -> 토네이도 방향 바꾸는 지표 -> 좌-하 : turn = 2 /우-상: turn = 4, 2씩 늘어난다.
    now = 0  
    proportion = proportions[0]        

    while not (tr == 0 and tc == 0):

        tr += delta[curl][0] 
        tc += delta[curl][1]
        now += 1   
        sand = data[tr][tc]
        data[tr][tc] = 0   
        left = sand

        for r in range(5): # 이해 안 가는 부분
            for c in range(5):
                now_sand = int(sand * proportion[r][c])
                left -= now_sand
                if 0 <= tr + r - 2 < N and 0 <= tc + c - 2 < N:                                 # data 배열 안에 가능하다면 data 갱신
                    data[tr + r - 2][tc + c - 2] += now_sand
                else:                                                                           # 불가능 하다면 밖으로 나간 모래
                    outer_sand += now_sand

        if 0 <= tr + alphas[curl][0]- 2 < N and 0 <= tc + alphas[curl][1] - 2 < N:
            data[tr + alphas[curl][0] - 2][tc + alphas[curl][1] - 2] += left
        else:
            outer_sand += left

        if now == turn // 2 or now == turn:
            curl = (curl + 1) % 4
            proportion = proportions[curl]
            if now == turn:
                now = 0
                turn += 2

    print(outer_sand)
    return


N = int(input())
sr = sc = N//2 
data = [list(map(int, input().split())) for _ in range(N)]
solution()