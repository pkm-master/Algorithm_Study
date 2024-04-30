# 타인의 코드
from copy import deepcopy  
from itertools import permutations
  
N, M, K = map(int, input().split())  
arr1 = [[*map(int, input().split())] for _ in range(N)]  
rotate = [[*map(int, input().split())] for _ in range(K)]  

order = list(permutations(rotate, K))  # 회전 연산 순서 순열  

result = [[0]*M for _ in range(N)]  # 결과저장 배열  

cnt = float('inf')  # 최소값 저장  
  
for k in range(len(order)):  # 순열 길이만큼 반복  
    arr = deepcopy(arr1)  # 초기 배열로 돌아가기 
    result = deepcopy(arr)
    for l in range(K):  # K개의 회전 배열만큼 반복  
  
        sti = order[k][l][0] - order[k][l][2] - 1  
        stj = order[k][l][1] - order[k][l][2] - 1  
        endi = order[k][l][0] + order[k][l][2] - 1  
        endj = order[k][l][1] + order[k][l][2] - 1  
          
        while sti <= endi and stj <= endj:  # 내부 반복 while문
            for i in range(sti, endi+1):  # 회전 시켜줄 네모부터 반복  
                for j in range(stj, endj+1):  
                    # 시작 행과 행이 같다면 좌 -> 우  
                    # 첫 시작점은 밑에서 들고와야되서 배제 해주기                    
                    if i == sti and j != stj:  
                        result[i][j] = arr[i][j-1]  
                    # 종료 열과 열이 같다면 위에서 아래  
                    elif j == endj and i != sti:  
                        result[i][j] = arr[i-1][j]  
                    # 종료 행과 같다면 우 -> 좌  
                    elif i == endi and j != endj:  
                        result[i][j] = arr[i][j+1]  
                    # 시작열과 같다면 하 -> 상  
                    elif j == stj and i != endi:  
                        result[i][j] = arr[i+1][j]  
  
            # 다 채웠다면 내부로 들어가기  
            sti += 1  
            stj += 1  
            endi -= 1  
            endj -= 1  
        
        arr = deepcopy(result)  # 여러 번 회전 위한 배열 deepcopy  
  
    for b in result:  # 최소값 구하기
        cnt2 = sum(b)  
        if cnt2 < cnt:  
            cnt = cnt2
  
print(cnt)