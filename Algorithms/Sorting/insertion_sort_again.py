arr = [648564,654,6486,46,45,4354,3545,48646,5,464,8,654,5,31,231,35,4648,65,54,64,864,54,366]

for i in range(1, len(arr)):
    key = arr[i]
    j = i-1
    
    while j >= 0 and key < arr[j]:
        arr[j+1] = arr[j]
        j -= 1
    
    arr[j+1] = key

print(arr)