def simulate_game(N, H, ladder):
    for i in range(1, N + 1):
        current_pos = i
        for a, b in ladder:
            if b == current_pos:
                current_pos = a
            elif b + 1 == current_pos:
                current_pos = a + 1
        if current_pos != i:
            return False
    return True

def solve(N, M, H, ladder_info):
    min_additional_lines = float('inf')

    stack = []
    for i in range(1, H + 1):
        for j in range(1, N):
            stack.append((i, j))
    
    from itertools import combinations
    for additional_lines in range(4):
        for combination in combinations(stack, additional_lines):
            ladder = ladder_info.copy()
            ladder.extend(combination)
            if simulate_game(N, H, ladder):
                min_additional_lines = min(min_additional_lines, additional_lines)
    
    if min_additional_lines > 3:
        return -1
    else:
        return min_additional_lines

N, M, H = map(int, input().split())
ladder_info = []
for _ in range(M):
    a, b = map(int, input().split())
    ladder_info.append((a, b))

result = solve(N, M, H, ladder_info)
print(result)