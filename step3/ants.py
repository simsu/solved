import sys
input = sys.stdin.readline
stick, n = map(int, input().split())
arr = list()
for i in range(n):
    line = input().rstrip('\n')
    arr.append(int(line))
minTime, maxTime = 0, 0

for i in arr:
    minTime = max(minTime, min(i, stick - i))
    maxTime = max(maxTime, max(i, stick - i))

print(minTime, maxTime)