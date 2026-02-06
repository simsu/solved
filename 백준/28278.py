import sys
input = sys.stdin.readline

n = int(input())

class Stack:
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        return -1 if self.empty() == 1 else self.stack.pop()
    def num(self):
        return len(self.stack)
    def empty(self):
        return 1 if self.num() == 0 else 0
    def top(self):
        return -1 if self.empty() == 1 else self.stack[-1]

def solve():
    stack = Stack()
    answer = []
    for _ in range(n):
        line = input().split()
        i = line[0]
        if i == '1':
            stack.push(line[1])
        elif i == '2':
            answer.append(str(stack.pop()))
        elif i == '3':
            answer.append(str(stack.num()))
        elif i == '4':
            answer.append(str(stack.empty()))
        elif i == '5':
            answer.append(str(stack.top()))
    sys.stdout.write('\n'.join(answer)+'\n')

solve()
