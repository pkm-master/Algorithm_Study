'''
백준 14889 스타트와 링크

n 명을 두팀으로 나눠 팀 구성
팀별 능력치 차가 최소값이 되도록 

swea의 요리사 문제랑 비슷
'''

def dfs(n, a, b):
    global ans

    if n == N:
        if len(a) == len(b):
            a_sum = 0
            b_sum = 0
            for i in range(N//2):
                for j in range(N//2):
                    a_sum += arr[a[i]][a[j]]
                    b_sum += arr[b[i]][b[j]]
            ans = min(ans, abs(a_sum - b_sum))
        return

    dfs(n+1, a+[n], b)
    dfs(n+1, a, b+[n])

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 10e9

dfs(0, [], [])

print(ans)