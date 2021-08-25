# 백준 다음 팰린드롬수 문제
# https://www.acmicpc.net/status?user_id=hansx2079&problem_id=1334&from_mine=1

N = str(int(input()) + 1)
nLen = len(N)
k = nLen//2

if nLen == 1:
    print(N)
else:
    if int(N[k-1::-1]) < int(N[nLen-k:nLen]): 
        N = str(int(N) + 10**k)
    print(N[:nLen-k] + N[k-1::-1])