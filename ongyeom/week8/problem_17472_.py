# 다른 사람 풀이

def find(x):
    if parent[x] < 0:
        return x
        
    parent[x] = find(parent[x])
    return parent[x]
    
def union(a, b):
    root_a = find(a)
    root_b = find(b)
    
    if root_a == root_b:
        return False
    
    if parent[root_a] < parent[root_b]:
        parent[root_b] = root_a
    elif parent[root_a] > parent[root_b]:
        parent[root_a] = root_b
    else:
        parent[root_a] = root_b
        parent[root_b] -= 1
    
    return True

# 상하좌우로 한 칸 이동
def move():
    yield (-1, 0)
    yield (1, 0)
    yield (0, -1)
    yield (0, 1)

# BFS로 섬 마다 번호 부여하고, 각각의 섬에 속하는 좌표들을 그룹핑
def BFS(start_x, start_y, island_num):
    visited[start_x][start_y] = True
    q = deque([(start_x, start_y)])
    island_search[(start_x, start_y)] = island_num
    island_cdns.append((island_num, start_x, start_y))
    
    while q:
        x, y = q.pop()
        
        for dx, dy in move():
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == 1 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    island_search[(nx, ny)] = island_num
                    island_cdns.append((island_num, nx, ny))
                    q.appendleft((nx, ny))

N, M = map(int, input().split())
board = []

for _ in range(N):
    board.append([*map(int, input().split())])

visited = [[False]*M for _ in range(N)]
island_search = dict() # 어떤 좌표가 어느 섬에 속하는지 조회
island_cdns = [] # 땅인 모든 좌표들
island_num = 0 # 섬 번호 붙일 때 사용(모두 붙이고 나면, 이 변수는 총 섬의 개수를 의미)

for row in range(N):
    for col in range(M):
        if board[row][col] == 1 and visited[row][col] == False:
            island_num += 1
            BFS(row, col, island_num)

edges = [] # MST 후보 간선들 모아놓는 리스트

# MST 후보 간선 모으는 코드
# 모든 땅 좌표를 순회하면서, 상하좌우 네 방향으로 모두 뻗어나가서,
# 다른 섬과 다리 건설이 가능하면 그 간선을 edges에 저장
for num, x, y in island_cdns:
    for dx, dy in move():
        nx = x + dx
        ny = y + dy
        dist = 0 # 다리 길이 기록
        island_fin = None # 다른 섬 도착 여부와 도착한 섬의 번호를 의미
        
        while True:
            # 방문한 땅이 같은 섬에 속한 땅일 경우 이 방향은 다리 건설 불가능
            if island_search.get((nx, ny)) == num:
                break
            
            # 방문하려는 좌표가 지도를 벗어날 때 break 해주기
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                break
            
            # 방문한 땅이 다른 섬에 속한 땅일 때
            if island_search.get((nx, ny)) != None and island_search.get((nx, ny)) != num:
                island_fin = island_search.get((nx, ny))
                break
            
            nx += dx
            ny += dy
            dist += 1
        
        # 기록한 길이가 2 이상이고, 다른 섬에 도착한 경우
        if dist >= 2 and island_fin != None:
            edges.append((dist, num, island_fin))

edges.sort(reverse=True)
parent = [-1]*(island_num+1)
cnt = island_num-1
res = 0

# N-1개의 유효한 간선을 사용하여 MST를 만들 때까지 반복
while cnt:
    # 만약 모든 간선을 다 pop했는데도 아직 MST를 만들지 못한 경우
    try:
        w, n1, n2 = edges.pop()
    except:
        res = -1
        break
    
    if union(n1, n2):
        res += w
        cnt -= 1

print(res)