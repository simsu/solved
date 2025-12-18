import sys
input = sys.stdin.readline

a = str(input())
b = str(input())

digit = 1
dump = 0
answer = 0

for i in range(2, -1, -1):
    arr = []
    result = 0
    for j in range(2, -1, -1):
        units = int(b[i]) * int(a[j]) + dump
        if units >= 10:
            dump = units // 10
            units %= 10
        else:
            dump = 0
        arr.append(str(units))
    if dump > 0:
        arr.append(str(dump))
        dump = 0
    result = int(''.join(x for x in arr[::-1]))
    answer += result * digit
    digit *= 10
    print(result)
    arr.clear()
print(answer)
