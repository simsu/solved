# 시간초과
import time

start = time.time()
x = int(input())

a, b = 0, -1
c, d = 0, 0

for i in range(1, x+1):
    b += 1
    if b == a:
        a += 1
        b = 0
c = a - b
d = b + 1
if a%2 == 0:
    d, c = c, d
else:
    pass
print(f"{c}/{d}")
end = time.time()

print(f"time: {end-start:.5f} sec")
