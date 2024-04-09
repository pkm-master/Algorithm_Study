'''
21610 마법사 상어와 비바라기

N * N 칸은 연결되어 있다
좌, 좌상, 상, 우상, 우, 우하, 하, 좌하 순으로 이동방향
구름이 있는 칸은 물이 1 증가
구름이 사라짐
줄이 증가한 칸 기준 대각선 방향으로 거리 1인 칸에 물이 있는 수 만큼 물 양 증가(경계 넘어간다고 대각선 방향 1이 아님)
물이 2 이상인 모든 칸에 구름 생성(직전에 구름이 사라진 칸에는 생기지 않음) 물 2 차감
M번 이동 후 물의 양의 합
'''
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cloud = [(N-1,0),(N-1,1),(N-2,0),(N-2,1)]    # 구름초기위치

di = [0, 0, -1, -1, -1, 0 , 1, 1, 1]
dj = [0, -1, -1, 0, 1, 1, 1, 0, -1]

# M번  반복
for _ in range(M):  
    # 구름이동, 물 증가, 구름사라짐
    D, S = map(int, input().split())
    
    # 이동할 구름의 위치(좌표)저장
    cloud2 = []              
    
    for ci,cj in cloud:
        # 양쪽끝이 연결되어 있으므로
        ni = (ci + di[D] * S + N) % N
        nj = (cj + dj[D] * S + N) % N 
        # 물 증가
        arr[ni][nj]+=1      
        cloud2.append((ni,nj))

    # 구름 이동한 위치에서 대각선체크
    visit = [[0]*N for _ in range(N)]
    
    for ci,cj in cloud2:
        # 구름위치 표시
        visit[ci][cj]=1         
        
        for dii,djj in ((-1,-1),(-1,1),(1,-1),(1,1)):
            ni = ci + dii
            nj = cj + djj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] > 0:
                arr[ci][cj]+=1

    # 전체순회 물 2이상, 구름발생(물 - 2), 단 cloud2위치 제외
    cloud = []
    
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 2 and visit[i][j] == 0:
                arr[i][j] -= 2
                cloud.append((i,j))
ans = 0

for i in arr:
    ans += sum(i)
print(ans)