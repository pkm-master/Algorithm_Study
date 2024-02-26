n,m = map(int,input().split())
temp = list(map(int,input().split()))
sumval = [0]*(n-m+1)
sumval[0] = sum(temp[:m])
max_sum = sumval[0]

for i in range(1,n-m+1):
    sumval[i] = sumval[i-1] - temp[i-1] + temp[i+m-1]
    if max_sum<sumval[i]:
        max_sum  = sumval[i]

print(max_sum)
