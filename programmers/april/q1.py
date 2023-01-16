
def solution(absolute, signs):
    ret = 0
    for i in range(len(absolute)):
        if signs[i]:
            ret += absolute[i]
        else:
            ret -= absolute[i]
    return ret

if __name__ == "__main__":
    example = []
    for n, expected_result in example:
        print("My Result : ", solution(n))
        print("Correct Result : ", expected_result)
        print()