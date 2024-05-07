dr = [0,-1,1,0,0]
dc = [0,0,0,-1,1]

N,M,K = map(int,input().split())
res = M
arr = [list(map(int,input().split())) for _ in range(N)]
shark_direction = [0] + list(map(int,input().split()))

priority = [{} for _ in range(M+1)]

for i in range(1,M+1):
    for j in range(1,5):
        priority[i].setdefault(j,list(map(int,input().split())))

smell = [[[0,0,[]] for _ in range(N)] for _ in range(N)]
shark_locations = [[0,0] for _ in range (M+1)]
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0 :
            shark_locations[arr[i][j]] = [i,j]
            smell[i][j][2].append(arr[i][j])

t=0

while t<=1000:
    for index,shark_location in enumerate(shark_locations):
        if index == 0 :
            continue
        
        if shark_location[0] != -1 :
            smell[shark_location[0]][shark_location[1]][0] = index
            smell[shark_location[0]][shark_location[1]][1] = K

    for index,shark_location in enumerate(shark_locations):     
        if index == 0 :
            continue
        
        if shark_location[0] == -1 :
            continue
        
        for prior in priority[index][shark_direction[index]]:
            new_r = shark_location[0]+dr[prior]
            new_c = shark_location[1]+dc[prior]
            
            if 0<=new_r<N and 0<=new_c<N and smell[new_r][new_c][0] == 0 :
                smell[shark_location[0]][shark_location[1]][2].pop()
                shark_locations[index][0] = new_r
                shark_locations[index][1] = new_c
                shark_direction[index] = prior
                smell[new_r][new_c][2].append(index)
                
                break 
            
        else :
            for prior in priority[index][shark_direction[index]]:
                new_r = shark_location[0]+dr[prior]
                new_c = shark_location[1]+dc[prior]
                
                if 0<=new_r<N and 0<=new_c<N and smell[new_r][new_c][0] == index :
                    smell[shark_location[0]][shark_location[1]][2].pop()
                    shark_locations[index][0] = new_r
                    shark_locations[index][1] = new_c
                    shark_direction[index] = prior
                    smell[new_r][new_c][2].append(index)
                
                    break 
    
    # 같은 자리의 상어 없애기 + 냄새 없애기
    for i in range(N):
        for j in range(N):
            if smell[i][j][0] != 0 :
                smell[i][j][1] -= 1 
                if smell[i][j][1] == 0 :
                    smell[i][j][0] = 0
            
            smell[i][j][2].sort()
            while len(smell[i][j][2])>1 :
                shark = smell[i][j][2].pop()
                shark_locations[shark][0] = -1
                res -= 1 
    
    t += 1
    
    if res == 1 :
        break 
    

else :
    t = -1
    

print(t)
    


