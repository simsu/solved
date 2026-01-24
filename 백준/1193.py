x = int(input())

a,b = 1,1

while x>a:
    b += 1
    a += b

d = a - x
an1 = b - d
an2 = d + 1
if b%2 == 1:
  an1, an2 = an2, an1
print(f"{an1}/{an2}")
