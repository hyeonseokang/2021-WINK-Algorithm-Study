# 풀었는데 왜 깃헙에 이것만 안올라갔지???

def solution(n, arr1, arr2): 
    answer = []
    for i in range(n):
        m = arr1[i] | arr2[i]
        bit = bin(m)[2:]
        bit = '0'*(n - len(bit)) + bit
        
        result = bit.translate(str.maketrans('10', '# '))
        answer.append(result)
            
    return answer