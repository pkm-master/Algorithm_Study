'''
백준 2559 수열

문제 해석
입력 - n(온도를 측정한 전체 날짜), k(연속적 날짜)
출력 - 가장 큰 합

문제 풀이 절차
아이디어
연속 합을 구해서 max값 출력
'''
#시간 초과
# n, k = map(int,input().split())
# nums = list(map(int, input().split()))

# a = 0

# for i in range(n-k+1):
#     x = sum(nums[i:i+k])
#     if a < x:
#         a = x

# print(a)

n, k = map(int,input().split())
x = list(map(int,input().split()))
a = maxa = sum(x[:k])


for i in range(k,n):
    a = a + x[i] - x[i-k]
    maxa = max(maxa, a)
print(maxa)