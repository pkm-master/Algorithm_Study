w,h = map(int,input().split())
st = tuple(map(int,input().split()))
t = int(input())

x = (st[0]+t) % (2*w)
y = (st[1]+t) % (2*h)

print(x if x<=w else 2*w-x)
print(y if y<=h else 2*h-y)