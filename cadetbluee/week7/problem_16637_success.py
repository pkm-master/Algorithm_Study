import sys
N = int(sys.stdin.readline())
cal = list(sys.stdin.readline().strip())
result = -1*2**31 # 최솟값

def calculate(a, op, b):
    if op=='+':
        num = a + b
    elif op=='*':
        num = a * b
    elif op == '-':
        num = a - b
    return num   

def dfs(index, target):
    global result

    if index == N - 1:
        result = max(result, target)
        return

    if index + 2 < N:
        next_value = calculate(target, cal[index + 1], int(cal[index + 2])) 
        dfs(index + 2, next_value) 

    if index + 4 < N:

        next_next_value = calculate(int(cal[index+2]), cal[index+3], int(cal[index+4]))
        next_value = calculate(target, cal[index + 1], next_next_value) 
        dfs(index + 4, next_value) 

dfs(0, int(cal[0]))
print(result)