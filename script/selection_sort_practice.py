# https://www.acmicpc.net/problem/11399
# bigO: n^2
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

def sol(n_list):
    sorted_n_list = selection_sort(n_list)
    waiting_time = 0
    total_time = 0
    for t in sorted_n_list:
        waiting_time = waiting_time+t
        total_time = total_time + waiting_time
    return total_time

if __name__ == '__main__':
    n = int(input())
    n_list = list(map(int,input().split()))
    print(sol(n_list))
