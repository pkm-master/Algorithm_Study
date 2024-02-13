fir = int(input())
sec = fir
maxlist = []

def check(fir, sec):
    nlist = [fir, sec]
    while 1:
        num = fir - sec
        if num < 0:
            break
        nlist.append(num)
        fir = sec
        sec = num
    return nlist

while True :
    cnt = check(fir,sec)
    if len(maxlist) < len(cnt):
        maxlist = cnt
    sec -= 1
    
    if sec < 0 :
        break

print(len(maxlist))
print(*maxlist)