'''
백준 2116 주사위 쌓기

문제 해석
입력 - 주사위 개수, 주사위 중류
출력 - 첫줄에 한 옆면의 숫자의 합이 가장 큰 값

보통 주사위처럼 마주 보는 면의 숫자 합이 7이 아니다.
주사이 쌓을 때 규칙
붙는 면의 숫자는 같아야한다.

문제 풀이 절차
아이디어
전개도 0 5, 1 3, 2 4가 마주보는 면
'''
n = int(input())
dice = [list(map(int, input().split()) for i in range(n))]
maxsum = 0

#몰라 포기