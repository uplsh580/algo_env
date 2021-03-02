# Ploblem : [하노이 탑 이동 순서] https://www.acmicpc.net/problem/11729

# Solver : Seonghwan Lee
# Solved Date : 2021-02-25
# BigO: 2^N

pos_1 = 0b100
pos_2 = 0b010
pos_3 = 0b001
count = 0

def trans_pos (pos):
    if pos == pos_1:
        return 1
    elif pos == pos_2:
        return 2
    elif pos == pos_3:
        return 3
    return 0 # Error!


def hanoi(f, t, n):
    global count
    m = 0b111 ^ (f | t)
    if n == 1:
        count += 1
        return [[f, t]]
    elif n == 2:
        count += 3
        return [[f, m], [f, t], [m, t]]
    else:
        count += 1
        ret = hanoi(f, m, n-1) + [[f,t]] + hanoi(m, t, n-1)
        return ret


if __name__ == '__main__':
    n = int(input())
    moves = hanoi(pos_1, pos_3, n)
    print(count)
    for m in moves:
        print('{} {}'.format(trans_pos(m[0]), trans_pos(m[1])))
