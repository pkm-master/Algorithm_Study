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