# 10158 개미

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

x = 1
y = 1
i = p
j = q

for _ in range(t):

    if i == w:
        x = -1
    elif i == 0:
        x = 1
    
    if x == 1:
        i += 1
    elif x == -1:
        i -= 1
        
    if j == h:
        y = -1
    elif j == 0:
        y = 1
    
    if y == 1:
        j += 1
    elif y == -1:
        j -= 1
    
print(i,j)

#시간 초과