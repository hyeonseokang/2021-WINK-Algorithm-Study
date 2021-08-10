# 프로그래머스 K번째수
# https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    
    for i, j, k in commands:
        a = sorted(array[i - 1: j])
        answer.append(a[k-1])
        
    return answer