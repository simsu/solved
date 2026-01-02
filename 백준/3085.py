import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

number = int(input())
board = [list(input().strip()) for _ in range(number)]
board_copy = [row[:] for row in board]

def count_candy():
    prev_max, cur_max = 1, 1
    for col in range(number):
        for row in range(number):
            if row == number-1:
                prev_max = max(prev_max, cur_max)
                cur_max = 1
                break
            if board_copy[col][row] == board_copy[col][row+1]:
                cur_max += 1
            else:
                prev_max = max(prev_max, cur_max)
                cur_max = 1
    for row in range(number):
        for col in range(number):
            if col == number-1:
                prev_max = max(prev_max, cur_max)
                cur_max = 1
                break
            if board_copy[col][row] == board_copy[col+1][row]:
                cur_max += 1
            else:
                prev_max = max(prev_max, cur_max)
                cur_max = 1
    return prev_max

def swap_candy(a, b):
    temp = board_copy[a[0]][a[1]]
    board_copy[a[0]][a[1]] = board_copy[b[0]][b[1]]
    board_copy[b[0]][b[1]] = temp
    return

def find_candy(a, b):
    swap_candy(a, b)
    candy = count_candy()
    swap_candy(a, b)
    return candy

def main():
    max_candy = 0
    for col in range(number):
        for row in range(number):
            if row + 1 < number:
                if board[row][col] != board[row+1][col]:
                    cur_candy = find_candy((row, col), (row+1, col))
                    max_candy = max(max_candy, cur_candy)
            if col + 1 < number:
                if board[row][col] != board[row][col+1]:
                    cur_candy = find_candy((row, col), (row, col+1))
                    max_candy = max(max_candy, cur_candy)
            if max_candy >= number: # 최대 개수 도달
                return number
    return max_candy
    
print(main())
