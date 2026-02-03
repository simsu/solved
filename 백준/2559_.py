n, k = map(int,input().split())
arr = list(map(int,input().split()))
# 10개를 n개로 묶으면 n-k+1개 묶음이 나온다. (시간 초과)
max_sum = -10000001
arr_sum = []
for i in range(n-k+1):
    max_sum = max(max_sum, sum(arr[i:i+k]))
print(max_sum)
