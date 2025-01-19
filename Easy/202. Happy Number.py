n = 7
sum = 0
s = set()
while sum != 1:
    for i in str(n):
        sum += int(i)
    if sum == 1:
        print(True)
    else:
        if sum in s:
            print(False)
            break
        else:
            s.add(sum)
            n = sum
            sum = 0

# Better Solution

def is_happy(n):
    def _next(num):
        total = 0
        while num > 0:
            d = num % 10
            total += d ** 2
            num //= 10
        return total

    seen = set()
    seen.add(n)

    while True:
        n = _next(n)
        if n == 1:
            return True
        if n in seen:
            return False
        seen.add(n)
