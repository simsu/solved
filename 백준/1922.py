import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input())
computer_num = [i for i in range(1, n+1)]

m = int(input())
cost = [list(map(int, input().split())) for i in range(m)]
parent = [i for i in range(1, n+1)]
cost.sort(key=lambda x: x[2])
result = 0

def find(x):
    if parent[x-1] == x:
        return x
    return find(parent[x-1])

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b-1] = a

for a, b, c in cost:
    if find(a) != find(b):
        union(a, b)
        result += c

print(result)
