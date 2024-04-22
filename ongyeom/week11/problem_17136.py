# 타인의 코드
board = [list(map(int, input().split())) for _ in range(10)]
papers = [0, 5, 5, 5, 5, 5] # 남아있는 색종이 개수 배열
result = set()


# 색종이 최대 길이 구하는 함수
def find_length(y, x):
    length = 1
    for l in range(2, min(10 - y, 10 - x, 5) + 1): # 배열 범위를 벗어나는 것을 방지하기 위해 min 함수 사용
        for i in range(y, y + l):
            for j in range(x, x + l):
                if board[i][j] == 0:
                    return length
        length += 1
    return length


# 색종이 덮는 함수
def cover(y, x, length):
    for i in range(y, y + length):
        for j in range(x, x + length):
            board[i][j] = 0


# 색종이 치우는 함수
def uncover(y, x, length):
    for i in range(y, y + length):
        for j in range(x, x + length):
            board[i][j] = 1


def dfs(cnt):
    for i in range(0, 10):
        for j in range(0, 10):
            if board[i][j] == 1:
                length = find_length(i, j)
                for l in range(length, 0, -1):
                    if papers[l]:
                        cover(i, j, l)
                        papers[l] -= 1
                        result.add(dfs(cnt + 1))
                        uncover(i, j, l)
                        papers[l] += 1
                if result:
                    return min(result)
                else: # 결과 집합에 요소가 없을 경우 모든 칸을 채우지 못한 것으로 -1을 반환
                    return -1
    return cnt


result.add(dfs(0))
if -1 in result:
    result.remove(-1)
print(min(result) if result else -1)