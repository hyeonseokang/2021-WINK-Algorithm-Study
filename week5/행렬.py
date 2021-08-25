# 백준 행렬 문제
# https://www.acmicpc.net/problem/1080

count = 0
n, m = [int(i) for i in input().split()]

A = [list(map(int, input())) for _ in range(n)] 
B = [list(map(int, input())) for _ in range(n)]

def reverse(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            A[i][j] = 1 - A[i][j]

for i in range(0, n-2):
    for j in range(0, m-2):
        if A[i][j] != B[i][j]:
            reverse(i, j)
            count += 1

if A != B:
    count = -1

print(count) 


N = input()
nLen = len(N)
k = nLen//2
 
if int(N[k-1::-1]) > int(N[nLen-k:nLen]):
    print(N[:nLen-k] + N[k-1::-1])
else:
    a = nLen-k-1
    if N[a] == '9':
        N = str(int(N) + 10**k)
        print(N[:nLen-k] + N[k-1::-1])
    else:
        print(N[:a] + str(int(N[nLen-k-1]) + 1) + N[k-1::-1])
