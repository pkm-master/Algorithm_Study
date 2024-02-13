# DP로 푸는 문제
# 작은 부분집합의 결과들로 큰 부분집합의 결과를 만듦

N= int(input())

result=[0]*(N+1)

for i in range (2,N+1):
    result[i]=result[i-1]+1   #연산1: 1을 뺀다
    
    if i%2==0:
        result[i] = min(result[i],result[i//2]+1)  #연산2: 2로 나누어떨어지면 2로 나눈다
    if i%3==0:
        result[i]= min(result[i],result[i//3]+1)   #연산3: 3으로 나누어 떨어지면 3으로 나눈다
        
print(result[N])

# ex)
# N=2   N=3      N=4
# [1]   [1,1]    [1,1,2]
# N=4  ->  4/2   ,  2/2   => N이 2일때 연산에서 한번 더 계산하면됨(result[i//2]+1)