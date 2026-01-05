import sys 
import heapq

n, m = map(int, sys.stdin.readline().split())
jewels = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
bags = [int(sys.stdin.readline()) for _ in range(m)]

jewels.sort(key=lambda x: x[0])
bags.sort()

answer = 0
heap = []
idx = 0

# 이중 for문으로 했더니 시간 초과 엔딩..
for bag in bags:
    while idx < n and jewels[idx][0] <= bag:
        heapq.heappush(heap, -jewels[idx][1]) # 최소힙만 가능하므로
        idx += 1
    if heap:
        answer += -heapq.heappop(heap)

print(answer)
