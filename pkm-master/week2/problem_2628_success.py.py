n,m = map(int,input().split())
tc = int(input())

cutted_i = []
cutted_j = []

for _ in range(tc):
    cut_n,cut = map(int,input().split())
    if cut_n :
        cutted_j.append(cut)  
    else : 
        cutted_i.append(cut)

cutted_j.sort()
cutted_i.sort()
new_i = []
new_j = []

if cutted_i :
    new_i.append(cutted_i[0])
    for i in range(1, len(cutted_i)):
        new_i.append(cutted_i[i]-cutted_i[i-1]) 
    new_i.append(m-cutted_i[-1])

if cutted_j :
    new_j.append(cutted_j[0])
    for j in range(1,len(cutted_j)):
        new_j.append(cutted_j[j]-cutted_j[j-1])
    new_j.append(n-cutted_j[-1])    

total_sum = []

if new_i and new_j :
    for i in new_i:
        for j in new_j:
            total_sum.append(i*j)
elif new_i :
    for i in new_i :
        total_sum.append(i*n)
elif new_j :
    for j in new_j:
        total_sum.append(j*m)
else : 
    total_sum = [n*m]

print(max(total_sum))
    
    
    