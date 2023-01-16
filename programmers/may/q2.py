def solution(numbers):
    answer = []

    for e in numbers:
        bit_checker = 0b1
        if e & bit_checker == 0:
            answer.append(e+bit_checker)
            continue
        
        bit_checker *= 2
        flag_pre_one = True
        
        while  e >= bit_checker//2:
            if e & bit_checker == 0:
                if flag_pre_one == True:
                    answer.append(e+bit_checker - (bit_checker//2))
                    break
                flag_pre_one == False
            else:
                flag_pre_one == True

            bit_checker *= 2

    return answer

print(solution([0, 1, 2, 3, 7]))