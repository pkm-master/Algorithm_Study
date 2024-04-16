# 다른 사람 풀이
n , fireball , order = map(int, input().split())

graph = [[[] for _ in range(n)] for _ in range(n)]

for i in range(fireball):
    x, y , m, s, d = map(int, input().split())
    x, y = x-1, y - 1
    graph[x][y].append([m,s,d])

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(order):
    new_graph = [[[] for _ in range(n)] for _ in range(n)]
    # 이동 수행
    for i in range(n):
        for j in range(n):
            if len(graph[i][j]) != 0:
                while graph[i][j]:
                    ## 질량, 속도, 방향
                    m, s, d = graph[i][j].pop()
                    nx = i + dx[d] * s
                    ny = j + dy[d] * s
                    nx = nx % n
                    ny = ny % n
                    new_graph[nx][ny].append([m, s, d])
    # 파이어볼 생성
    for i in range(n):
            for j in range(n):
                if len(new_graph[i][j]) > 1:
                    total_m = 0
                    total_s = 0
                    total_d = []
                    while new_graph[i][j]:
                        m, s, d = new_graph[i][j].pop()
                        total_m += m
                        total_s += s
                        total_d.append(d)
                    ## 새로운 질량, 속도
                    next_m = total_m // 5
                    if next_m == 0:
                        pass
                    else: 
                        next_s = total_s // len(total_d)
                        checker = 0
                        num = total_d.pop()
                        # 짝수 검사
                        if num % 2 == 0:
                            while total_d:
                                next_num = total_d.pop()
                                if next_num % 2 == 0:
                                    continue
                                else:
                                    checker = 1
                                    break
                        # 홀수 검사
                        else:
                            while total_d: 
                                next_num = total_d.pop()
                                if next_num % 2 == 1:
                                    continue
                                else:
                                    checker = 1
                                    break
                        if checker == 0:
                            for k in range(4):
                                graph[i][j].append([next_m, next_s, k * 2])
                        else:
                            for k in range(4):
                                graph[i][j].append([next_m, next_s, (k * 2 + 1)])
                elif len(new_graph[i][j]) == 1:
                    graph[i][j].append(new_graph[i][j].pop())
                    
total_fireball = 0

for i in range(n):
    for j in range(n):
        if len(graph[i][j]) != 0:
                while graph[i][j]:
                    # print(graph[i][j])
                    m, s, d = graph[i][j].pop()
                    total_fireball += m

print(total_fireball)