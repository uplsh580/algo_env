# Ploblem : [하노이 탑 이동 순서] https://www.acmicpc.net/problem/1914

# Solver : Seonghwan Lee
# Solved Date : 2021-02-25
# BigO: N^2 (n<=20), N (20<n)

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


def hanoi_count(n):
    l = [1]
    if n != 1:
        for i in range(1,n):
            l.append(l[-1] * 2 + 1)
    return l[-1]
if __name__ == '__main__':
    n = int(input())
    if n <= 20:
        moves = hanoi(pos_1, pos_3, n)
        print(count)
        for m in moves:
            print('{} {}'.format(trans_pos(m[0]), trans_pos(m[1])))
    else:
        print(hanoi_count(n))
