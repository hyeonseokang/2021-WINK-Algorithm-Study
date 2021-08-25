# 프로그래머스 다리를 지나는 트럭 문제
# https://programmers.co.kr/learn/courses/30/lessons/42583

def solution(bridge_length, weight, truck_weights):
    count = 1
    
    c_weight = 0
    c_trucks = []

    while True:
        if c_trucks == [] and truck_weights == []:
            return count
            
        if len(truck_weights) > 0 and truck_weights[0] + c_weight <= weight:
            truck = truck_weights.pop(0)
            c_trucks.append((truck, count))
            c_weight = truck + c_weight
        
        count += 1    
        if c_trucks[0][1] + bridge_length == count:
            truck = c_trucks.pop(0)
            c_weight -= truck[0]
            
            
    return -1