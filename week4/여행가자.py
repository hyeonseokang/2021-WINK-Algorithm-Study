# 백준 여행가자
# https://www.acmicpc.net/problem/1976

n = int(input())
m = int(input())

maps = []

for i in range(n):
    maps.append(list(map(int, input().split())))
    maps[i][i] = 1

order = list(map(lambda i:int(i)-1, input().split()))

for _ in range(3):
    temp_maps = [[0 for i in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                temp_maps[i][j] += maps[i][k] * maps[k][j]
    maps = temp_maps

result = 'YES'
for i in range(len(order)-1):
    if maps[order[i]][order[i+1]] <= 0:
        result = 'NO'
        break

print(result)

