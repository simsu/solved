def solution(nums):
    unique_nums = len(set(nums))
    answer = 0
    if unique_nums > len(nums) // 2:
        answer = len(nums) // 2
    else:
        answer = unique_nums
    return answer

nums = [3,3,3,2,2,4]
print(solution(nums))
