arr = [54,64,86,34,34,354,354,866,84,34,354,534684]

for i in range(1, len(arr)):
    key = arr[i]
    j = i-1
    while j >= 0 and key < arr[j]:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key
print(arr)    