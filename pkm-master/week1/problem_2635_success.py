initial = int(input())
ls = [''] * 30001
ls[0] = initial
max_cnt = 0
max_ls = []

for i in range(initial+1) :
    ls[1] = i
    j = 2
    new = 0
    while ls[j-1] >= 0 :
        ls[j] = ls[j-2]-ls[j-1]
        j+=1
    cnt = j-1
    if max_cnt < cnt :
        max_cnt = cnt
        max_ls = ls[:]
    
print(max_cnt)
print(*list(map(str,max_ls[:max_cnt])))