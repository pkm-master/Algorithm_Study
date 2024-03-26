# 게리맨더링 2
def cal(x, y, d1, d2):
    elec = [0 for i in range(5)]
    temp = [[0] * (n + 1) for i in range(n + 1)]

    for i in range(d1 + 1): 
        temp[x + i][y - i] = 5
        temp[x + d2 + i][y + d2 - i] = 5
        
    for i in range(d2 + 1):
        temp[x + i][y + i] = 5
        temp[x + d1 + i][y - d1 + i] = 5

    for i in range(x + 1, x + d1 + d2):
        flag = False
        
        for j in range(1, n + 1):
            if temp[i][j] == 5: 
              flag = not flag 
            if flag: 
              temp[i][j] = 5

    for r in range(1, n + 1):
        for c in range(1, n + 1):
            if r < x + d1 and c <= y and temp[r][c] == 0:  
              elec[0] += graph[r][c]
              
            elif r <= x + d2 and y < c and temp[r][c] == 0:  
              elec[1] += graph[r][c] 
              
            elif x + d1 <= r and c < y - d1 + d2 and temp[r][c] == 0: 
              elec[2] += graph[r][c] 
              
            elif x + d2 < r and y - d1 + d2 <= c and temp[r][c] == 0: 
              elec[3] += graph[r][c] 
              
            elif temp[r][c] == 5:  
              elec[4] += graph[r][c] 
              
    return max(elec) - min(elec)
  
n = int(input())
graph = [[]]
ans = 1e9
for i in range(n): 
  graph.append([0] + list(map(int, input().split())))

for x in range(1, n + 1):
    for y in range(1, n + 1):
        for d1 in range(1, n + 1):
            for d2 in range(1, n + 1):
                if 1 <= x < x + d1 + d2 <= n and 1 <= y - d1 < y < y + d2 <= n:
                    ans = min(ans, cal(x, y, d1, d2))
print(ans)