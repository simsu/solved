# 완주자를 dict로 바꾸고 동명이인인 경우 value를 증가시킨다.
# 이후 참가자를 돌면서 완주자명에 없거나 동명이인 value가 0인 경우 리턴한다.
def solution(participant, completion):
    runners = {}
    for i in completion:
        if runners.get(i):
            runners[i] += 1
        else:
            runners[i] = 1
    for i in participant:
        if not runners.get(i) or runners.get(i) == 0:
            return i
        else:
            runners[i] -= 1

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant, completion))
