arr = [1,9,10,15,23,39,41]

l = 0
r = len(arr)-1

target = 10

while l <= r:
    mid = (l+r)//2
    if arr[mid] == target:
        print(mid)
        break
    elif arr[mid] < target:
        l = mid + 1
    elif arr[mid] > target:
        r = mid - 1
else:
    print(-1)