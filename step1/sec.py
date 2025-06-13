import sys
input = sys.stdin.readline

DTIME = 60*60*24
HTIME = 60*60
MTIME = 60

sec = int(input())
d, h, m, s = 0, 0, 0, 0
d = sec//DTIME
sec %= DTIME
h = sec//HTIME
sec %= HTIME
m = sec//MTIME
sec %= MTIME
s = sec
print(d, h, m, s)