# 배운점: itertools 모듈, 튜플 순회 방법
# 공집합을 포함해서 찾으면 풀기 쉬웠던...
from itertools import combinations


def solution(clothes):
    wearable = dict()
    for cloth in clothes:
        if cloth[1] in wearable:
            wearable[cloth[1]] += 1
        else:
            wearable[cloth[1]] = 1
    answer = 1
    for i in wearable.keys():
        answer *= (wearable[i]+1)
    return answer-1 # -1의 이유: 모두 공집합인 경우를 빼야한다.

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"], ["blue_hat", "headgear"], ["yellow_ring", "ring"], ["gray_ring", "ring"]]
print(solution(clothes))
