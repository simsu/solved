import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for i in range(n)]
result = [[0] * n for i in range(n)]
visited = set()

def dfs(num, start):
    for i in range(n):
        if graph[num][i] == 1 and i not in visited:
            visited.add(i)
            dfs(i, start)
    for x in visited:
        result[start][x] = 1

for i in range(n):
    dfs(i, i)
    visited.clear()

for i in result:
    print(' '.join(map(str, i)))
