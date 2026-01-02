import sys
import os
sys.stdin = open(os.path.basename(__file__).split('.')[0] + '.txt', "r")

T = int(input())
for test_case in range(1, T + 1):
    answer = 0
    numbers = list(map(int, input().split()))
    for num in numbers:
        if  num%2 == 1:
            answer += num
    print(f"#{test_case} {answer}")

'''
출력:
#1 200
#2 208
#3 121
'''
