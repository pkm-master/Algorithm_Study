for _ in range(4):
    arr = list(map(int, input().split()))
    a,b,c,d = arr[:4]
    A,B,C,D = arr[4:]

    result ='a'
    if a > C or A > c or b > D or B > d:
        result = 'd'

    elif a == C:
        if b == D or B == d :
            result = 'c'
        else:
            result = 'b'
    elif b == D:
        if a == C or A == c :
            result = 'c'
        else:
            result = 'b'
    elif A == c:
        if b == D or B == d:
            result = 'c'
        else:
            result = 'b'
    elif B == d:
        if a == C or A == c :
            result = 'c'
        else :
            result = 'b'

    print(result)
