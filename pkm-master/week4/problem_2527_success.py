for _ in range(4):
    
    x1,y1,p1,q1,x2,y2,p2,q2 = map(int,input().split())
    
    olx = max(x1,x2)
    olp = min(p1,p2)
    oly = max(y1,y2)
    olq = min(q1,q2)
    
    if olp-olx < 0 or olq-oly < 0 :
        print('d')
    elif olp-olx == 0 and olq-oly == 0 :
        print('c')
    elif olp-olx == 0 or olq-oly == 0 :
        print('b')
    else : 
        print('a')
    