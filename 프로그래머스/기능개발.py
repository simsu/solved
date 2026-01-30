# 나는 슬라이스했는데 다른 풀이보니까 pop하는게 더 좋은것 같기도 하다.
import math

def solution(progresses, speeds):
    answer = []
    while len(progresses) > 0 :
        count = 0
        day = math.ceil((100 - progresses[0]) / speeds[0])
        i = 0
        while i < len(progresses):
            if progresses[i] + speeds[i] * day >= 100:
                count += 1
            else:
                break
            i += 1
        progresses = progresses[i:]
        speeds = speeds[i:]
        answer.append(count)
    return answer


progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses, speeds))  # [2, 1]
