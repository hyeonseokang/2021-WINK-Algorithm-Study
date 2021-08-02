# 프로그래머스 가장 큰 수 문제
# https://programmers.co.kr/learn/courses/30/lessons/42746
def solution(numbers):
    numbers = list(map(str, numbers))
    
    sort_lambda = lambda i: i * 4
    numbers = sorted(numbers, key = sort_lambda, reverse = True)

    if set(numbers) == {'0'}:
        return '0'
    
    return ''.join(numbers)