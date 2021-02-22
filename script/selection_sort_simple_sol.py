# Ploblem: https://www.acmicpc.net/problem/2752
# [Required] Use the Selection Sort to solve it.

# Solver: Seonghwan Lee
# Solved Date: 2021-02-22
# BigO: N^2

def swap (l, a, b):
    temp = l[a]
    l[a] = l[b]
    l[b] = temp


def selection_sort(n_list):
    n = len(n_list)
    for i in range(n):
        temp_min_pos = i
        for j in range(i, n):
            if n_list[temp_min_pos] > n_list[j]:
                temp_min_pos = j
        if temp_min_pos != i:
            swap(n_list, i, temp_min_pos)

    return n_list

if __name__ == '__main__':
    n_list = list(map(int,input().split()))
    print(' '.join(map(str,selection_sort(n_list))))
