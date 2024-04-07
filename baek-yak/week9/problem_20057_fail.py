'''
마법사 상어와 토네이도

가운데 부터 토네이도 시작
한 칸 이동할 때 마다 일정한 비율로 흩날린다.
모래가 격자 밖으로 이동 할 수도 있다.
밖으로 나간 모래의 양을 구하자
'''
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
val = [[0]*N for _ in range(N)]

# 좌,하,우,상
di = [ 0, 1, 0,-1]
dj = [-1, 0, 1, 0]

ci = N//2
cj = N//2
ans = 0

while (ci,cj) != (0,0):
    # dr방향으로 이동
    ci = ci+di[dr]
    cj= cj+dj[dr]   

    # ci, cj 기준좌표 중심으로 모래량 계산, 범위 밖 ans에 추가
    # 모래가 있을때만 진행
    if arr[ci][cj]>0:
        val = arr[ci][cj]       
        arr[ci][cj] = sm = 0

