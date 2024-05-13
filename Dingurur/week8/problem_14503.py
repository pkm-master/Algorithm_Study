def clearmyroom(r, c, d):
    global cnt
    if visited[r][c] == 0:
        visited[r][c] = 1
        cnt += 1

    for _ in range(4): # 네 방향에 대해서 확인
        nd = (d + 3) % 4  # 현재 방향 기준으로 반시계 방향으로 회전
        nr = r + dirs[nd][0]
        nc = c + dirs[nd][1]
        if 0 <= nr < N and 0 <= nc < M and Arr[nr][nc] == 0 and visited[nr][nc] == 0:  # 네 방향에 아직 청소하지 않은 공간이 있으면
            clearmyroom(nr, nc, nd)
            return  # 청소하러 가고 함수 종료
        d = nd  # 회전만 한다

    # 네 방향 모두 청소할 곳이 없는 경우 후진
    nd = (d + 2) % 4  # 현재 방향 기준으로 후진
    nr = r + dirs[nd][0]
    nc = c + dirs[nd][1]
    if 0 <= nr < N and 0 <= nc < M and Arr[nr][nc] == 0:  # 후진할 수 있으면
        clearmyroom(nr, nc, d)
        return  # 후진 후 함수 종료
    elif 0>nr or N<=nr or 0>nc or M<=nr or Arr[nr][nc] != 0:
        return  # 후진할 수 없으면 종료

N, M = map(int, input().split())
r, c, d = map(int, input().split())
r -= 1 # 인덱스 보정
c -= 1
Arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]  # 청소한 곳을 표시할 배열
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북, 동, 남, 서
cnt = 0
clearmyroom(r, c, d)
print(cnt)
