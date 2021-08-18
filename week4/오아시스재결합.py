# 백준 오아시스 재결합
# https://www.acmicpc.net/problem/3015

n = int(input())
result = 0
s = []

for i in range(n):
    num = int(input())
    
    while s and s[-1][0] < num:
        result += s.pop()[1]
    
    total = 1
    if s:
        if s[-1][0] == num:
            result += s[-1][1]
            total += s.pop()[1]
        
    if s:
        result += 1    
        
    s.append((num, total))

print(result)