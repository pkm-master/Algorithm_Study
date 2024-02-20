Kk = input()
K = list(map(str,Kk))
ch = input()
Kn = len(K)
chn = len(ch)
arr = [[0]*(chn//Kn) for _ in range(Kn)]
c = 0
for i in range(Kn):
    for j in range(chn//Kn):
        arr[i][j] = ch[c]
        c += 1
K.sort()
for i in range(Kn):
    K[i] = (K[i], i)
K.sort(key=lambda x: Kk.index(str(x[0])))

# for i in range(Kn):
#     print(arr[K[i][1]])

for j in range(chn//Kn):
    for i in range(Kn):
        print(arr[K[i][1]][j], end="")