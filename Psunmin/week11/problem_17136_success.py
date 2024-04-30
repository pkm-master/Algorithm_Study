def func(x, y, cnt):
    global ans
    
    # y범위 넘어가면 탐색 끝
    if y >= 10:
        ans = min(ans, cnt)
        return

    # x범위 넘어가면 그 다음 줄 탐색
    if x >= 10:
        func(0, y+1, cnt)
        return

    if a[x][y] == 1:
        for k in range(5):
            # 색종이가 이미 있거나
            if paper[k] == 5:
                continue
            # x,y 범위 넘어가면 탐색 안함
            if x + k >= 10 or y + k >= 10:
                continue

            flag = 0
            # 해당 위치에 0있으면 색종이 못붙임
            for i in range(x, x + k + 1):
                for j in range(y, y + k + 1):
                    if a[i][j] == 0:
                        flag = 1
                        break
                if flag:
                    break
            
            # 색종이 붙일 수 있으면
            if not flag:
                for i in range(x, x + k + 1):
                    for j in range(y, y + k + 1):
                        a[i][j] = 0

                # 범위 1-5까지 다 붙일 수 있는지 확인
                paper[k] += 1
                func(x + k + 1, y, cnt + 1)
                paper[k] -= 1

                for i in range(x, x + k + 1):
                    for j in range(y, y + k + 1):
                        a[i][j] = 1
    else:
        func(x + 1, y, cnt)


a = [list(map(int, input().split())) for _ in range(10)]
paper = [0 for _ in range(5)]
ans = 1e9
func(0, 0, 0)
if ans <1e9:
    print(ans)
else:
    print(-1)
