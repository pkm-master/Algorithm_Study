'''
4번정도 시간 초과가 나고 두 세번 틀려서 포기한 문제입니다.
'''

def mins(n):
    cnt = 0
    while n != 1:
        if n % 3 == 0:
            n //= 3
        elif n % 3 == 1 :
            n -= 1
        elif n % 2 == 0:
            n //= 2
        else:
            n -= 1
        cnt += 1
    return cnt

n = int(input())
print(mins(n))