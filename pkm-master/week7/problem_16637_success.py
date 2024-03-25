import sys
sys.stdin = open('./input.txt')


def add_gwal(j,i,F) :

    global result

    if j==i:
        res = [0]*i
        for k in range(i) :
            a = F[2*path[k]]
            p = F[2*path[k]+1]
            b = F[2*path[k]+2]
            re = 0
            if p == '+' :
                re = int(a)+int(b)
            elif p == '-' :
                re = int(a)-int(b)
            else :
                re = int(a)*int(b)

            res[k] = re

        ope = '+*-'
        stk = []
        j=0
        cnt = 0

        while j < len(F) :
            if F[j] in ope :
                op = F[j]
                a = int(stk.pop())
                if (j+1)//2 in path :
                    b = res[cnt]
                    cnt+=1
                    j+=4
                else :
                    b = int(F[j+1])
                    j += 2

                if op == '+':
                    stk.append(a+b)
                elif op == '-' :
                    stk.append(a-b)
                else :
                    stk.append(a*b)

            else :
                if j//2 in path :
                    stk.append(res[cnt])
                    cnt+=1
                    j+=3
                else :
                    stk.append(int(F[j]))
                    j+=1

        if stk[-1] >result :
            result = stk[-1]
        return

    for n in range(len(F)//2) :
        if j>0 and path[j-1]>=n :
            continue
        if j>0 and n == path[j-1]+1:
            continue
        path[j] = n
        add_gwal(j+1,i,F)


N = int(input())
F = input()
result = -2**31
for i in range((N+1)//4+1) :
    path = [0]*i
    add_gwal(0,i,F)

print(result)
