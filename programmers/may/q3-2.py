def solution(s):
    answer = []
    
    for cur_s in s:
        ret_s = ""

        one_count = 0
        for c in cur_s:
            if c == "1":
                one_count += 1
            else: # '0'
                if one_count < 2:
                    ret_s += "1" * one_count
                    one_count = 0
                    ret_s += "0"
                else:
                    ret_s += "110"
                    one_count -= 2
        ret_s += "1" * one_count
        answer.append(ret_s)
    return answer

s = ["1"]
print(s)
print(solution(s))
print()