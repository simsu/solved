import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def binary_search(n_list, i):
    start, mid, end = 0, n//2, n-1
    while start <= end:
        if n_list[mid] == i:
            return 1
        elif n_list[mid] > i:
            end = mid - 1
        else:
            start = mid + 1
        mid = (start + end) // 2
    return 0


n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))
n_list.sort()
for i in m_list:
    result = binary_search(n_list, i)
    print(result)
