#17281 야구
'''
경기 시작전 타순 정해야함, 단 4번타자는 고정 1번선수
한 이닝에 3아웃 이닝 종료
9번 타자까지 공 치고  3아웃 아님 이닝 속행
아무 이닝에서 6번이 마지막이면 다음 이닝은 7번이 스타트


'''
n = int(input())
game = [list(map(int, input().split())) for _ in range(n)]

ans  = 0

order = [i for i in range(1,9)]

#모르겠음 3시간 붙잡고 있다 답을 봤는데도 하나도 감이 안잡히는