def fib(a,b, length):
    if a + b in arr:
        length += 1
        return fib(b, a+b, length)
    else:
        return length

arr = [1,2,3,4,5,6,7,8]
max_length = 0
for i, num in enumerate(arr[:-1]):  # No need to go to the last element since there's no next element
    current_length = 0
    for j in range(i+1, len(arr)):
        if num + arr[j] in arr:
            # current_length += 1
            # Capture the length from recursive calls
            current_length += fib(arr[j], num + arr[j], 1)  # Start length from 1 as we have a valid initial pair
            max_length = max(max_length, current_length)
print(max_length)