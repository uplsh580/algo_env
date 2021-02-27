# Ploblem : [피보나치 수 4] https://www.acmicpc.net/problem/10826

# Solver : Seonghwan Lee
# Solved Date : 2021-02-24
# BigO: N


def fibonacci_2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    ret_result = [1,1]
    for i in range(2,n):
        ret_result.append(ret_result[i-1] + ret_result[i-2])
    return ret_result[-1]


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_2(n))
