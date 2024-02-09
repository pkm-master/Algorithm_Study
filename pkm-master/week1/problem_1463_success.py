'''
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.

16 -> 8 -> 4 -> 2 -> 1
16 -> 15 -> 5 -> 4 -> 3 -> 1 

9 -> 3 -> 1

3으로 나눠떨어지는데 1빼면 2의 제곱수가되는경우..
33 -> 11 -> 10 -> 9 -> 3 -> 1 
33 -> 32 -> 16 -> 8 -> 4 -> 2 -> 1

정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.
'''


x = int(input())
if x<4 : 
    count = [0]*4
else : 
    count = [0]*(x+1)
count[1],count[2],count[3] = 0,1,1


for i in range(4,x+1):
    if i % 3 ==0 and i % 2 == 0 :
        count[i] = min(count[i//3], count[i//2], count[i-1])+1
    elif i%3==0:
        count[i] = min(count[i//3],count[i-1])+1
    elif i%2==0:
        count[i] = min(count[i//2],count[i-1])+1
    else : 
        count[i] = count[i-1]+1
    
print(count[x])