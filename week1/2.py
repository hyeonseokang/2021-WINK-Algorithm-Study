# 프로그래머스 기능개발 문제
# https://programmers.co.kr/learn/courses/30/lessons/42586

import math 

def progress_time(progress, speed):
    return math.ceil((100 - progress) / speed)

def solution(progresses, speeds):
    answer = []
    
    prev_time = progress_time(progresses[0], speeds[0])
    prev_index = 0
    total_time = prev_time
    
    for i in range(1, len(progresses)):
        current_time = progress_time(progresses[i], speeds[i])
        
        if current_time - total_time > 0:
            answer.append(i - prev_index)
            prev_index = i
            total_time = current_time

        prev_time = current_time
    
    answer.append(len(progresses) - prev_index)
        
    return answer