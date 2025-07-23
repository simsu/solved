import sys
input = sys.stdin.readline

# m = (r1 + r2) / 2
r1, m = map(int, input().split())
r2 = 0
if m == 0:
    r2 = r1
else:
    r2 = (2 * m) - r1
print(r2)
