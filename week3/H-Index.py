# 프로그래머스 H-Index 문제
# https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    citations.sort()
    
    length = len(citations)
    for idx, i in enumerate(citations):
        h = length - idx
        if i >= h:
            return h
        
    return 0
