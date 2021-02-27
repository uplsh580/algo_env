# Ploblem: [평균은 넘겠지] https://www.acmicpc.net/problem/4344

# Solver: Seonghwan Lee
# Solved Date: 2021-02-18
# BigO:

def solution(n, score):
    avg_score = sum(score)/n
    over_s = sum(1 for x in score if x > avg_score)
    return round((over_s/n) * 100,3)

if __name__ == '__main__':
    c = int(input())
    for i in range(c):
        args = list(map(int, input().split()))
        n = args[0]
        score = args[1:]

        print("{:.3f}%".format(solution(n, score)))