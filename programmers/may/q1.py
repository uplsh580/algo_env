def solution(left, right):
    answer = 0
    for cur in range(left, right + 1):
        count = 0
        for i in range(1, cur+1):
            if (cur % i) == 0:
                count += 1
        
        if (count%2) == 1:
            answer -= cur
        else:
            answer += cur
    return answer

print(solution(13, 17))
