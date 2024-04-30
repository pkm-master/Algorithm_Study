def jongi(paper):
    sizes = [5, 4, 3, 2, 1]
    count = 0

    for size in sizes:
        for i in range(10 - size + 1):
            for j in range(10 - size + 1):
                if paper[i][j] == 1:
                    coverable = True
                    for x in range(i, i + size):
                        for y in range(j, j + size):
                            if paper[x][y] == 0:
                                coverable = False
                                break
                        if not coverable:
                            break
                    if coverable:
                        count += 1
                        for x in range(i, i + size):
                            for y in range(j, j + size):
                                paper[x][y] = 0

    for row in paper:
        if 1 in row:
            return -1

    return count


paper = [list(map(int, input().split())) for _ in range(10)]

result = jongi(paper)
print(result)