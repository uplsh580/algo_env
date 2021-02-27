# Ploblem : [하노이 탑] https://www.acmicpc.net/problem/1914

# Solver : 
# Solved Date : 
# BigO: 

# Feel free to use.
pos_1 = 0b100
pos_2 = 0b010
pos_3 = 0b001
count = 0

# Feel free to use.
def trans_pos (pos):
    if pos == pos_1:
        return 1
    elif pos == pos_2:
        return 2
    elif pos == pos_3:
        return 3
    return 0 # Error!


# Feel free to change anything.
def hanoi(f, t, n):
    global count
    count += 1
    return [[f, t]]


if __name__ == '__main__':
    n = int(input())
    moves = hanoi(pos_1, pos_3, n)
    print(count)
    if count <= 20:
        for m in moves:
            print('{} {}'.format(trans_pos(m[0]), trans_pos(m[1])))
