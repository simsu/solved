num = int(input())
m = [list(input()) for _ in range(num)]

def swap_candy_x(row, col):
    m[row][col], m[row][col+1] = m[row][col+1], m[row][col]

def swap_candy_y(row, col):
    m[row][col], m[row+1][col] = m[row+1][col], m[row][col]

def count_x():
    max_count = 1
    for row in range(num):
        count = 1
        letter = m[row][0]
        for col in range(1, num):
            if m[row][col] == letter:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 1
                letter = m[row][col]
        max_count = max(max_count, count)
    return max_count

def count_y():
    max_count = 1
    for col in range(num):
        count = 1
        letter = m[0][col]
        for row in range(1, num):
            if m[row][col] == letter:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 1
                letter = m[row][col]
        max_count = max(max_count, count)
    return max_count

def search():
    return max(count_x(), count_y())

def compute_x(m):
    max_count = 1
    for row in range(num):
        for col in range(num-1):
            if m[row][col] == m[row][col+1]:
                continue
            swap_candy_x(row, col)
            max_count = max(max_count,search())
            swap_candy_x(row, col)
    return max_count

def compute_y(m):
    max_count = 1
    for col in range(num):
        for row in range(num-1):
            if m[row][col] == m[row+1][col]:
                continue
            swap_candy_y(row, col)
            max_count = max(max_count,search())
            swap_candy_y(row, col)
    return max_count

def main():
    print(max(compute_x(m), compute_y(m)))

if __name__ == "__main__":
    main()
