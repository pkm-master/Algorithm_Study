#게리맨더링2
N = int(input()) # 재현시 크기
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] #재현시 이차원 배열
total = 0
for row in matrix:
    total += sum(row) # 전체 인구수 계산

answer = int(1e9) # 결과값을 저장할 변수, 초기값은 아주 큰 값으로 설정

def calculate(row, col, d1, d2):
    global total, answer
    first, second, third, fourth = 0, 0, 0, 0

    # 구역 1 (r, c)에서 시작해서 오른쪽 위로 d1만큼 이동하는 구간 계산
    col1 = col+1
    for r in range(row+d1):
        if r >= row:
            col1 -= 1
        first += sum(matrix[r][:col1])

    # 구역 2 (r, c)에서 시작해서 오른쪽 아래로 d2만큼 이동하는 구간 계산
    col2 = col+1
    for r in range(row+d2+1):
        if r > row:
            col2 += 1
        second += sum(matrix[r][col2:])
   
    # 구역 3 (r, c)에서 시작해서 왼쪽 아래로 d1만큼 이동하는 구간 계산
    col3 = col - d1
    for r in range(row+d1, N):
        third += sum(matrix[r][:col3])
        if r < row+d1+d2:
            col3 += 1

    # 구역 4 (r, c)에서 시작해서 왼쪽 위로 d2만큼 이동하는 구간 계산
    col4 = (col+d2) - N
    for r in range(row+d2+1, N):
        fourth += sum(matrix[r][col4:])
        if r <= row+d1+d2:
            col4 -= 1
            
    # 구역 5 나머지 부분의 인구수 계산
    five = total - first - second - third - fourth
    # 각 구역의 인구수의 최대값과 최소값의 차이를 구하고, 최소값으로 업데이트
    answer = min(answer, (max(first, second, third, fourth, five) - min(first, second, third, fourth, five)))

def check(r, c, d1, d2): # 가능한 d1, d2 찾기
    if 0 <= r+d1-1 < N and 0 <= r+d2-1 < N and 0 <= c-d1+d2-1 < N:
        if 0 <= c-d1 and c+d2 < N and r+d1+d2 < N:
            calculate(r, c, d1, d2)

# 가능한 모든 구간에 대해 최소값을 구함
for r in range(N-2):
    for c in range(1, N-1):
        for d1 in range(1, N-1):
            for d2 in range(1, N-1):
                check(r, c, d1, d2)
print(answer)