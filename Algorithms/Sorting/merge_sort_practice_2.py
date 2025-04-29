arr = [21,534,34,35,4684,6,486,435,321,84,64,3]

def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]
    
    