for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    result = ''
    if p1<x2 or p2<x1 or q1<y2 or q2<y1:
        result = 'd'
    elif p1==x2 or p2==x1:
        if q1==y2 or q2==y1:
            result = 'c'
        else:
            result ='b'
    elif q1==y2 or q2==y1:
        result = 'b'
    else:
        result = 'a'
    print(result)

