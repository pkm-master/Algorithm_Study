for _ in range(4):
    x, y, p, q, x1, y1, p1, q1 = map(int, input().split())

    if x1 < p and x < p1 and y1 < q and y < q1:
        print("a")
    elif ((p == x1 or x == p1) and (y1 < q and y < q1)) or ((y == q1 or y1 == q) and (x1 < p and x < p1)):
        print("b")
    elif ((x == p1 or p == x1) and (y == q1 or q == y1)):
        print("c")
    else:
        print("d")
