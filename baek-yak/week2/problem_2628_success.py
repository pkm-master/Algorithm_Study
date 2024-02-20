'''
백준 2628 종이자르기

문제 해석
입력 - 종이 가로 세로 | 점선들의 수 | 가로 점선 - 0 & 점선 번호, 세로 점선 - 1 & 점선번호
출력 - 가장 큰 종이의 넓이

문제 풀이 절차
아이디어
가로 세로 처음, 끝, 잘린 점을 배열에 담는다.
점을 정렬함
점들의 간격을 구해서, max 값의 곱을 출력
'''
x, y = map(int , input().split()) #x 가로, y 세로

#점 담을 배열
xlist = [0, x]
ylist = [0, y]

n = int(input())
for i in range(n):
    #w 가로 세로 방향, d 점 좌표
    w, d = map(int, input().split())
    
    if w == 1:
        xlist.append(d)
    else:
        ylist.append(d)

xlist.sort()
ylist.sort()

xmax = []
for i in range(len(xlist) - 1):
    xmax.append(xlist[i+1]-xlist[i])
ymax = []
for i in range(len(ylist) - 1):
    ymax.append(ylist[i+1]-ylist[i])

print(max(xmax)*max(ymax))