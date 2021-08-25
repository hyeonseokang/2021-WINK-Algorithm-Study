# 백준 새앨범 문제
# https://www.acmicpc.net/problem/1424

N = int(input())
L = int(input())
C = int(input())
S = 1

for i in range(C//L, 0, -1):
    if i * L + i - 1 <= C:
        S = i
        break

if S % 13 == 0:
    S -= 1

NS = N//S
if N % S == 0:
    pass
elif N % S % 13 != 0 or (S-1%13 != 0 and N%S + 1 < S):
    NS += 1
else:
    NS += 2

print(NS)