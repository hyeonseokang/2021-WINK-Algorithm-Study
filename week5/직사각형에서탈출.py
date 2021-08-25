# 백준 직사각형에서 탈출 문제
# https://www.acmicpc.net/problem/1085

x, y, w, h = [int(i) for i in input().split()]

print(min(w-x, h-y, x, y))