arr = [648564,654,6486,46,45,4354,3545,48646,5,464,8,654,5,31,231,35,4648,65,54,64,864,54,366]

def merge_sort(arr):
    
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]
        
        merge_sort(left_arr)
        merge_sort(right_arr)
        
        i = 0
        j = 0
        k = 0
        
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        
        while i < len(left_arr):
            arr[k] = left_arr[i]
            k += 1
            i += 1
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            k += 1
            j += 1
        
    return arr

print(merge_sort(arr))
    