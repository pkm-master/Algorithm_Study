N = int(input())
ori_arr = [list(map(int,input().split())) for _ in range(N)]

def del_zero(ls) : 
    st = 0
    end = 1
    while end < N and st < N :
        if ls[st] == 0 and ls[end] == 0 :
            end += 1
        elif ls[st] == 0 :
            ls[end],ls[st] = ls[st],ls[end]
            st+=1
            end+=1
        else : 
            st+=1
            end+=1
            
    return ls

def merge(ls) : 
    st = 0
    end = 1
    while end < N and st < N :
        if ls[st] == ls[end] :
            ls[st] = 2*ls[st]
            ls[end] = 0
            st += 2
            end += 2
        else :
            st+=1
            end+=1
    return ls

def left(ls) : 
    for i in range(N) :
        ls[i] = del_zero(ls[i])
        ls[i] = merge(ls[i])
        ls[i] = del_zero(ls[i])
                
    return ls

def right(ls) : 
    for i in range(N) :
        ls[i] = ls[i][::-1]
        ls[i] = del_zero(ls[i])
        ls[i] = merge(ls[i])
        ls[i] = del_zero(ls[i])
        ls[i] = ls[i][::-1]
    
    return ls

def up(ls) :
    for i in range(N) : 
        sero_ls = [ls[j][i] for j in range(N)]
        sero_ls = del_zero(sero_ls)
        sero_ls = merge(sero_ls)
        sero_ls = del_zero(sero_ls)
        for j in range(N) : 
            ls[j][i] = sero_ls[j]

    return ls

def down(ls):
    for i in range(N) :
        sero_ls = [ls[j][i] for j in range(N)][::-1]
        sero_ls = del_zero(sero_ls)
        sero_ls = merge(sero_ls)
        sero_ls = del_zero(sero_ls)
        for j in range(N-1,-1,-1) : 
            ls[j][i] = sero_ls[N-1-j]

    return ls

def _2048(i,n):
    global global_max_num
    
    if i == n :
        arr = [ori_arr[k][:] for k in range(N)]
        
        for el in path :
            if el == 0 :
                arr = up(arr)
            elif el == 1 :
                arr = down(arr)
            elif el == 2 :
                arr = left(arr)
            else : 
                arr = right(arr)
        
        max_num = max([max(arr[el]) for el in range(len(arr))])
        if max_num > global_max_num :
            global_max_num = max_num
    
    else : 
        for j in range(4) :
            path[i] = j 
            _2048(i+1,n)
    

global_max_num = 0
path = [0] * 5
_2048(0,5)

print(global_max_num)