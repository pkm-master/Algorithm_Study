N = int(input()) #기둥 갯수
max_H = 0
arr = [0]*1001

for i in range(N) : 
    L,H = map(int,input().split())
    arr[L] = H
    if max_H < H:
        max_H = H
        max_idx = L

tmp_H = max_H
tmp_idx = max_idx
ans = max_H
st = max_idx+1

while max_H != 0 and st<1001 : #오른쪽에 대해 
    new_arr = arr[st:]
    max_H = max(new_arr)
    max_idx = new_arr.index(max_H)
    ans += max_H * (max_idx+1)
    st += max_idx+1

max_H = tmp_H
end = tmp_idx

while max_H != 0 and end>0 : #왼쪽에 대해 
    new_arr = arr[:end]
    max_H = max(new_arr)
    max_idx = new_arr.index(max_H)
    ans += max_H * (end - max_idx)
    end -= (end - max_idx)
    
print(ans)
