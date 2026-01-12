h, w = map(int, input().split())
blocks = list(map(int, input().split()))

water = 0
# 자신의 좌우를 살펴보고 최대 블록을 찾아서 2번째로 큰 값에서 본인 블록 높이를 빼면 빗물의 양이 된다.
for (idx, block) in enumerate(blocks):
    left_max_block = 0
    right_max_block = 0
    for i in range(0, idx+1):
        left_max_block = max(left_max_block, blocks[i])
    for j in range(idx, w):
        right_max_block = max(right_max_block, blocks[j])
    water += min(left_max_block, right_max_block) - block
print(water)
