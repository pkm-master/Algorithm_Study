import sys
sys.stdin = open('test.txt')

arr = [list(map(int, input().split())) for _ in range(5)]
seq = []
for _ in range(5):
    nums = list(map(int, input().split()))
    for n in nums:
        seq.append(n)
bingo = 0

for s in range(25):
    for i in range(5):
        for j in range(5):
            if arr[i][j] == seq[s]:
                arr[i][j] = 0

            if arr[i][j] == 0:
            if arr[j][i] == 0:
            if arr[i][i] == 0:
            if arr[i][4-i] == 0:



