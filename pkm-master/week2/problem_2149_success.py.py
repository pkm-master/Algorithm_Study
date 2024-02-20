key = list(input())
pw = input()
n = len(key)
m = len(pw)

mat = [[] for _ in range(n)]

for i in range(m):
    mat[i//(m//n)].append(pw[i])
    
for j in range(n):
    key[j] = (key[j],j)

key.sort()

arr = [[] for _ in range(n)]
for k in range(n) :
    arr[key[k][1]] = mat[k]

for i in range(m//n):
    for ele in arr :
        print(ele[i],end='')
    
