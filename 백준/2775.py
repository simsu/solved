n = int(input())
arr_floor = []
arr_num = []
for _ in range(n):
    arr_floor.append(int(input()))
    arr_num.append(int(input()))

max_floor, max_num = max(arr_floor), max(arr_num)
residents = [[0 for _ in range(max_num)] for _ in range(max_floor+1)]

for floor in range(max_floor+1):
    for num in range(max_num):
        if floor == 0:
            residents[0][num] = num + 1
        else:
            if num == 0:
                residents[floor][0] = 1
            else:
                residents[floor][num] = residents[floor - 1][num] + residents[floor][num - 1]

for i in range(n):
    print(residents[arr_floor[i]][arr_num[i]-1])
