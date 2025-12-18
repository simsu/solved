import sys
input = sys.stdin.readline

def comparefrac2(a, b, c, d):
    if a*d > b*c:
        return 1
    elif a*d == b*c:
        return 0
    elif a*d < b*c:
        return -1

def comparefrac(a, b, c, d):
    if a/b > c/d:
        return 1
    elif a/b == c/d:
        return 0
    elif a/b < c/d:
        return -1
a, b, c, d = map(int, input().split())
print(comparefrac2(a, b, c, d))
