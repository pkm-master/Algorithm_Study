'''
백준 19237 어른 상어 실패

자기 위치에 자기 냄새 뿌림
인접칸 이동 후 마킹(마킹은 k번 이동하면 사라짐)

아무 마킹이 안된 칸으로 이동
자신의 냄새가 있는 칸의 방향으로 이동

곂칠 경우 가장 작은 번호 가진 상어 제외 모두 삭제
1번 상어만 남는 시간 출력(1000초 넘으면 -1 출력)
'''
N,M,K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 상어 정보 저장, 초기 냄새
shark = [[0]*4 for _ in range(M)]
v = [[[-1]*2 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j]>0:
            sm = arr[i][j]-1
            # 상어번호,i,j,dr
            shark[sm] = [sm,i,j,0]              
            # 상어번호, 냄새
            v[i][j][0], v[i][j][1] = sm, K   

lst = list(map(int, input().split()))

# 상어마리수
for i in range(M):                  
    # 방향
    shark[i][3]=lst[i]                

# 방향 우선순위 테이블
d = [[[0]*4 for _ in range(5)] for _ in range(M)]    
for i in range(M):
    for j in range(1,5):
        d[i][j] = list(map(int,input().split()))

# 상,하,좌,우
di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]

# 1초~1000초
for ans in range(1, 1001):  
    # 상어 이동: 현재 방향, 빈칸 -> 자기냄새
    for i in range(len(shark)):
        sm, si, sj, sd = shark[i]
        
        for dr in d[sm][sd]:
            ni = si + di[dr]
            nj = sj + dj[dr]
            
            # 범위내 냄새가 없는 경우
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj][0] == -1:
                shark[i] = [sm, ni, nj, dr]
        
        # 빈칸이 없는 경우 => 내 냄새
        else:               
            for dr in d[sm][sd]:
                ni = si + di[dr]
                nj = sj + dj[dr]
                if 0 <= ni < N and 0 <= nj < N and v[ni][nj][0] == sm:
                    shark[i]=[sm, ni, nj, dr]
