# y, x = map(int, input().strip().split())
# q, p = map(int, input().strip().split())
# t = int(input())
# i = 1
# j = 1
# for tc in range(t):
#     p += i
#     q += j
#     if (p < 0 and q > y) or (p > x and q < 0) or (p > x and q > y) or (p < 0 and q < 0):
#         i *= (-1)
#         j *= (-1)
#         p += i * 2
#         q += j * 2
#     elif (p < 0 and q <= y) or (p > x and q >= 0):
#         i *= (-1)
#         j *= (-1)
#         p += i * 2
#     elif (p >= 0 and q > y) or (p <= x and q < 0):
#         i *= (-1)
#         j *= (-1)
#         q += j * 2
# print(q, p)

y, x = map(int, input().strip().split())
q, p = map(int, input().strip().split())
t = int(input())
p += t % (2*x)
q += t % (2*y)
if p > x: p = (2*x) - p
if q > y: q = (2*y) - q
if p < 0: p = -p
if q < 0: q = -q
print(q, p)