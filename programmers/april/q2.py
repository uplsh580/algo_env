def rotation(s, n):
    return  s[n:]+s[:n]

def solution(s):
    result = 0
    len_s = len(s)

    for n in range(len_s):
        cur_s = rotation(s, n)
        no_issue = True

        # {}
        lrg_open = 0
        lrg_close = 0
        # []
        mid_open = 0
        mid_close = 0
        # ()
        sml_open = 0
        sml_close = 0


        for c in cur_s:
            if c == '{':
                lrg_open += 1
            elif c == '}':
                lrg_close += 1
                if lrg_open < lrg_close:
                    no_issue = False
                    break
            
            elif c == '[':
                mid_open += 1
            elif c == ']':
                mid_close += 1
                if mid_open < mid_close:
                    no_issue = False
                    break

            elif c == '(':
                sml_open += 1
            elif c == ')':
                sml_close += 1
                if sml_open < sml_close:
                    no_issue = False
                    break
                
        if lrg_open != lrg_close:
            no_issue = False
        if mid_open != mid_close:
            no_issue = False
        if sml_open != sml_close:
            no_issue = False
        if no_issue == True:
            result += 1

    return result


print(solution('[](){}'))