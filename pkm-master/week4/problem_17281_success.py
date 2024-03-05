from itertools import permutations  
N = int(input()) 
max_ans = 0

lss = [list(map(int,input().split())) for _ in range(N)]

for el in permutations(range(1,9),8) :
    tot_sc = 0
    idx = 0
    ls = el[:3] + (0,) + el[3:] 
        
    for i in range(N) : 
        cnt = 0
        field = [0]*3
        while cnt < 3 :
            n = lss[i][ls[idx]]
            if n == 0 :
                cnt+=1
            elif n == 1 :
                tot_sc += field[2]
                field = [1,field[0],field[1]]

            elif n == 2 :
                tot_sc += field[1]+field[2]
                field = [0,1,field[0]]

            elif n == 3 :
                tot_sc += field[0]+field[1]+field[2]
                field = [0,0,1]

            elif n == 4 :
                tot_sc += field[0]+field[1]+field[2] + 1
                field = [0,0,0]
                
            idx = (idx+1)%9
            
    if max_ans < tot_sc :
        max_ans = tot_sc

print(max_ans)