index = len(digits) - 1
        
def add(digits, index):
    if index < 0:
        digits.insert(0, 1)
        return digits
    if digits[index] < 9:
        digits[index] += 1
        return digits
    else:
        digits[index] = 0
        return add(digits, index - 1)  # Recursively call add for the next left digit

return add(digits, index)
