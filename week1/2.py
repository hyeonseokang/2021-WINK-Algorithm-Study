# 프로그래머스 기능개발 문제
# https://programmers.co.kr/learn/courses/30/lessons/42586

import math 

def progress_time(progress, speed):
    return math.ceil((100 - progress) / speed)

def solution(progresses, speeds):
    answer = []
    
    prev_t = progress_time(progresses[0], speeds[0])
    prev_index = 0
    t = prev_t
    
    for i, (p, s) in enumerate(zip(progresses, speeds)):
        current_t = progress_time(p, s)
        
        if current_t > t:
            answer.append(i - prev_index)
            prev_index = i
            t = current_t

        prev_t = current_t
    
    answer.append(len(progresses) - prev_index)
        
    return answer