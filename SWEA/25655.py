import sys
import os
sys.stdin = open(os.path.basename(__file__).split('.')[0] + '.txt', "r")

T = int(input())

for test_case in range(1, T + 1):
    number = int(input())
    answer = ''
    if number == 1:
        answer += '0'
    else:
        while number > 0:
            if number == 1:
                answer += '4'
                number -= 1
            if number>=2:
                number -= 2
                answer += '8'
    print(answer[::-1])

'''
출력:
0
8
8888888888888888
48
488
4888
488888
'''
