# 다른 사람 코드 참고

dir = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

N, M, K = map(int, input().split())
fire_list = []
fire = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r, c, m, s, d = list(map(int, input().split()))
    fire_list.append([r,c,m,s,d])
    
result = []

for _ in range(K):
    while fire_list:
        cr,cc,cm,cs,cd = fire_list.pop(0)
        nr = (cr+cs*dir[cd][0])%N
        nc = (cc+cs*dir[cd][1])%N
        fire[nr][nc].append([cm,cs,cd])

    for r in range(N):
        for c in range(N):
            if len(fire[r][c])>1:
                sum_m, sum_s, cnt_odd, cnt_even, cnt = 0, 0, 0, 0, len(fire[r][c])
                while fire[r][c]:
                    mm, ss, dd = fire[r][c].pop(0)
                    sum_m += mm
                    sum_s += ss
                    if dd % 2:
                        cnt_odd += 1
                    else:
                        cnt_even += 1
                if cnt_odd == cnt or cnt_even == cnt:
                    nd = [0,2,4,6]
                else:
                    nd = [1,3,5,7]
                if sum_m//5:
                    for id in nd:
                        fire_list.append([r, c, sum_m//5, sum_s//cnt, id])
            if len(fire[r][c]) == 1:
                fire_list.append([r, c] + fire[r][c].pop())
print(sum([r[2] for r in fire_list]))