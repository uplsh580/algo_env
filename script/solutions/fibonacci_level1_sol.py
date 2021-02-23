# Ploblem : [피보나치 수 5] https://www.acmicpc.net/problem/10870

# Solver : Seonghwan Lee
# Solved Date : 2021-02-24
# BigO: 2^N


def fibonacci_1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_1(n-1) + fibonacci_1(n-2)


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_1(n))
