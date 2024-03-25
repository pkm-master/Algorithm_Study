# 괄호 추가하기

N= int(input())

fx = list(input())

ans = int(-1e9)

def cal(k, check):
    if k == 0:
        global ans
        
        answer = [fx[0]]
        
        for i in range(len(fx)):
            if not fx[i].isdigit():
                if check[i//2] == 1:
                    answer = answer[:-1] + [str(eval(''.join(fx[i-1:i+2])))]
                else:
                    answer = answer + fx[i:i+2]

        while len(answer) > 1: 
            answer = [str(eval(answer[0]+answer[1]+answer[2]))] + answer[3:]
        
        if int(answer[0]) > ans:
            ans = int(answer[0])

    else :
        if not check or check[-1] == 0: 
            cal(k-1, check+[1])
        
        cal(k-1, check+[0])

cal(N//2, [])

print(ans)