import sys
input = sys.stdin.readline
amount = 1000 - int(input())
c1, c2, c3 = 0, 0, 0

c1 = amount // 100
amount %= 100
c2 = amount // 50
amount %= 50
c3 = amount // 10
print(c1, c2, c3)