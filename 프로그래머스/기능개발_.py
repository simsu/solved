import math
from collections import deque

def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    answer = []
    while len(progresses) > 0 :
        count = 0
        day = math.ceil((100 - progresses[0]) / speeds[0])
        while progresses[0] + speeds[0] * day >= 100:
            count += 1
            progresses.popleft()
            speeds.popleft()
            if len(progresses) == 0:
                break
        answer.append(count)
    return answer


progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses, speeds))  # [2, 1]
