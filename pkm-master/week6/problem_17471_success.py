from collections import deque

N = int(input())
N_P = [0] + list(map(int,input().split()))
adj = [[]] + [list(map(int,input().split()))[1:] for _ in range(N)]
min_ans = 100*10

for i in range(1<<N) :
    sec1 = []
    sec2 = []
    visited = [True] + [False] * N
    for j in range(N) :
        if 1<<j & i :
            sec1.append(j+1)
        else :
            sec2.append(j+1)

    if len(sec1) > 0 and len(sec2) > 0 :
        q = deque()
        q.append(sec1[0])
        q.append(sec2[0])
        visited[sec1[0]] = True
        visited[sec2[0]] = True

        while q :
            st = q.popleft()
            if st in sec1 :
                for ad in adj[st] :
                    if ad in sec1 and not visited[ad] :
                        q.append(ad)
                        visited[ad] = 1
            else :
                for ad in adj[st]:
                    if ad in sec2 and not visited[ad] :
                        q.append(ad)
                        visited[ad] = 1

    if False not in visited :
        ans = 0
        for idx,el in enumerate(N_P) :
            if idx in sec1 :
                ans-=el
            else :
                ans+=el
        ans = abs(ans)
        if ans < min_ans:
            min_ans = ans

if min_ans == 100*10 :
    min_ans = -1

print(min_ans)

