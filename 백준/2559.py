n, k = map(int,input().split())
arr = list(map(int,input().split()))
# 10개를 n개로 묶으면 n-k+1개 묶음이 나온다.
# 0~n까지 누적 합에서 0~m까지 누적합을 빼면 m~n까지 누적합이 나온다.
max_sum = -10000001
arr_sum = [0, ]
for i in range(n):
    arr_sum.append(arr_sum[i]+arr[i])
for i in range(n-k+1):
    max_sum = max(max_sum, arr_sum[i+k]-arr_sum[i])
print(max_sum)
