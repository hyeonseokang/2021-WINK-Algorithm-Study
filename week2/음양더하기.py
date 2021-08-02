# 프로그래머스 음양 더하기 문제
# https://programmers.co.kr/learn/courses/30/lessons/76501#

def solution(absolutes, signs):
    answer = 0
    
    for absolute, sign in zip(absolutes, signs):
        answer += absolute * (-1 + (sign * 2))
        
    return answer