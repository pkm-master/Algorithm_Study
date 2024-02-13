arr = [[0 for _ in range(100)] for __ in range(100)]
for _ in range(4):
    x1,y1,x2,y2 = tuple(map(int,input().split()))
    for i in range(y1,y2):
        for j in range(x1,x2):
            arr[i][j] = 1

sum_arr = [ sum(ls) for ls in arr ]
print(sum(sum_arr))