M, N = map(int, input().split())
C = int(input())
arr = [[0]*M for _ in range(N)]
i = [0]
j = [0]
for c in range(C):
    rc, cut = map(int, input().split())
    if rc == 0:
        i.append(cut)
    else:
        j.append(cut)
i.append(N)
j.append(M)
i.sort()
j.sort()
ri = []
rj = []
for ii in range(len(i)-1):
    ri.append(i[ii+1]-i[ii])
for jj in range(len(j)-1):
    rj.append(j[jj+1]-j[jj])
max_area = 0
for ai in ri:
    for aj in rj:
        area = ai*aj
        if max_area < area:
            max_area = area
print(max_area)