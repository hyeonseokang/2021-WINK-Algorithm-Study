# 프로그래머스 폰켓몬 문제
# https://programmers.co.kr/learn/courses/30/lessons/1845?language=python3

def solution(nums):
    num_set = set(nums)
    answer = min(len(nums) // 2, len(num_set))
    
    return answer