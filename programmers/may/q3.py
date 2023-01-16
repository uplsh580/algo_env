def solution(s):
    answer = []
    
    for cur_s in s:
        origin_s = ''
        while origin_s != cur_s:
            origin_s = cur_s
            index_110 = cur_s.rfind('110')
            cur_s = cur_s[:index_110] + cur_s[index_110+3:]

            index_111 = cur_s.find('111')
            if index_111 == -1:
                if cur_s == '1' or cur_s == '11':
                    cur_s = '110'+cur_s
                else:
                    cur_s += '110'

            else:
                cur_s = cur_s[:index_111] + '110' + cur_s[index_111:]

        answer.append(cur_s)
    return answer

s = ["1110","100111100","0111111010"]
print(solution(s))