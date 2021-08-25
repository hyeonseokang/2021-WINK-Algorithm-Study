# 백준 N번째 큰수
# https://www.acmicpc.net/problem/2075

n = int(input())
numbers = []

for i in range(n):
    numbers += list(map(int, input().split()))
    numbers = sorted(numbers, reverse=True)[:n]

print(numbers[-1])