# Ploblem: [연속합2] https://www.acmicpc.net/problem/13398

# Solver: Seonghwan Lee
# Solved Date: 2021-03-05
# BigO: N

def mss(n, seq):
    max_val = seq[0]
    cur_max = seq[0]
    cur_max_rmv = seq[0]

    for e in seq[1:]:
        cur_max_rmv = max(cur_max_rmv+e, cur_max+e, cur_max, e)
        cur_max = max(cur_max+e, e)
        max_val = max(max_val, cur_max, cur_max_rmv)


    cur_max = seq[-1]
    cur_max_rmv = seq[-1]

    for e in seq[-2::-1]:
        cur_max_rmv = max(cur_max_rmv+e, cur_max+e, cur_max, e)
        cur_max = max(cur_max+e, e)
        max_val = max(max_val, cur_max, cur_max_rmv)

    return max_val

if __name__ == '__main__':
    n = int(input())
    seq = list(map(int, input().split()))
    print(mss(n, seq))
