'''
배열 돌리기4
지정된 범위의 가로 세로는 2s
s 만큼 회전함

좌 하 우 상 회전 할 때 (r-s, c-s+1) 비정상 -> (r-s, c-s) 값을 저장하고 회전 후 값을 (r-s, c-s+1) 대입
'''

from itertools import  permutations
import copy
import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

arr = [[]]

for _ in range(n):
    arr.append([0] + list(map(int, input().split())))

x = []

for _ in range(k):
    x.append(list(map(int, input().split())))

def rotate(o, graph):
    r, c, s = o

    for j in range(s):
        tmp = graph[r - s + j][c - s + j]
        
        # 좌
        for i in range(r - s + j, r + s - j):
            graph[i][c - s + j] = graph[i + 1][c - s + j]

        # 하
        for i in range(c - s + j, c + s-j): 
            graph[r + s - j][i] = graph[r + s - j][i+1]

        # 우
        for i in range(r + s - j, r - s + j, -1): 
            graph[i][c + s - j] = graph[i - 1][c + s - j]

        # 상
        for i in range(c + s - j, c - s + j, -1): 
            graph[r - s + j][i] = graph[r - s + j][i - 1]

        graph[r - s + j][c - s + 1 + j] = tmp



maxV = int(1e9)
for z in permutations(x):
    g = copy.deepcopy(arr)

    for i in z:
        rotate(i, g)

    for i in range(1,n+1):
        maxV = min(maxV, sum(g[i]))

print(maxV)
