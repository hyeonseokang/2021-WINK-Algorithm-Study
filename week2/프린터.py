# 프로그래머스 프린터 문제
# https://programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    sort_arr = sorted(priorities, reverse = True)
    priorities = list(enumerate(priorities))
    
    i = 0
    length = len(priorities)
    count = 1
    
    while True:
        if priorities[i][1] != sort_arr[0]:
            i = (i + 1) % length
        else:
            if priorities[i][0] == location:
                return count
            
            priorities.pop(i)
            sort_arr.pop(0)
            length -=1
            i = i % length
            count += 1
    
    return count