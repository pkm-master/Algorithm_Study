w,h=map(int,input().split())
p,q=map(int,input().split())
t=int(input())

a = (p + t) // w  # 증가하는 부분인지 감소하는 부분인지 확인
b = (q + t) // h  # 증가하는 부분인지 감소하는 부분인지 확인

if a % 2 == 0:  # 해당 값이 증가하는 부분이라면
    x = (p + t) % w
else:  # 해당 값이 감소하는 부분이라면
    x = w - (p + t) % w

if b % 2 == 0:  # 해당 값이 감소하는 부분이라면
    y = (q + t) % h
else:  # 해당 값이 감소하는 부분이라면
    y = h - (q + t) % h

print(x, y)

'''
다른 풀이
w,h=map(int,input().split())
p,q=map(int,input().split())
t=int(input())

x=t%(2*w)
y=t%(2*h)

if x<=w-p:
    p+=x
elif x<=2*w-p:
    p=w-(x-w+p)
else:
    p=x-2*w+p

if y<=h-q:
    q+=y
elif y<=2*h-q:
    q=h-(y-h+q)
else:
    q=y-2*h+q

print(p,q)
'''