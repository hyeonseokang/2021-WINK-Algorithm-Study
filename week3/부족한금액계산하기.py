# 프로그래머스 부족한 금액 계산하기 문제
# https://programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    answer = price * (count * (count + 1) / 2) - money

    return max(answer, 0)