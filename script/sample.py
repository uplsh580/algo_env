# Ploblem : [평균은 넘겠지] https://www.acmicpc.net/problem/4344

# Solver: 
# Solved Date: 
# BigO:

def solution(n, score):
    return 0

if __name__ == '__main__':
    c = int(input())
    for i in range(c):
        args = list(map(int, input().split()))
        n = args[0]
        score = args[1:]

        print("{:.3f}%".format(solution(n, score)))
