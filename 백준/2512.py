num = int(input())
num_list = list(map(int, input().split()))
budget = int(input())

num_list.sort()
require_budget = sum(num_list)
max_budget = 1000000000

def isFit(max_num):
    current_budget = budget
    over_count = 0
    for i in num_list:
        if i <= max_num:
            current_budget -= i
        else:
            over_count += 1
            current_budget -= max_num
    if current_budget >= over_count:
        return 1
    elif current_budget < over_count and current_budget >= 0:
        return 0
    else:
        return -1

def main():
    if budget >= require_budget:
        max_budget = num_list[num-1]
        return max_budget

    start, end, mid = 0, 100000, int(num/2)
    max_budget = mid

    # 이진 탐색으로 예산 근접값 찾기
    while start!=mid and end!=mid:
        direction = isFit(max_budget)
        if direction == 1:
            start = mid
            mid = int((start+end)/2)
        elif direction == -1:
            end = mid
            mid = int((start+end)/2)
        elif direction == 0:
            return max_budget
        max_budget = mid

    # 디테일하게 찾기
    while direction != 0:
        direction = isFit(max_budget)
        if direction == 1:
            max_budget += 1
        elif direction == -1:
            max_budget -= 1
    return max_budget


print(main())
