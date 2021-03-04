# Ploblem: [연속합] https://www.acmicpc.net/problem/1912

# Solver: Seonghwan Lee
# Solved Date: 2021-03-03
# BigO: N

def mss(n, seq):
    max_val = seq[0]
    cur_max = seq[0]
    for e in seq[1:]:
        cur_max = max(cur_max+e, e)
        max_val = max(max_val, cur_max)

    cur_max = seq[-1]
    for e in seq[-2::-1]:
        cur_max = max(cur_max+e, e)
        max_val = max(max_val, cur_max)

    return max_val

if __name__ == '__main__':
    n = int(input())
    seq = list(map(int, input().split()))
    print(mss(n, seq))