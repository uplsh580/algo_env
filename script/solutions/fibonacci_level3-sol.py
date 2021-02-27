# Ploblem : [피보나치 수 3] https://www.acmicpc.net/problem/2749

# Solver : Seonghwan Lee
# Solved Date : 2021-02-24
# BigO: lonN

unit_mat = [[1,1],[1,0]]

def matmul22(mat1, mat2):
    e00 = (mat1[0][0] * mat2[0][0] + mat1[0][1] * mat2[1][0]) % 1000000
    e01 = (mat1[0][0] * mat2[0][1] + mat1[0][1] * mat2[1][1]) % 1000000
    e10 = (mat1[1][0] * mat2[0][0] + mat1[1][1] * mat2[1][0]) % 1000000
    e11 = (mat1[1][0] * mat2[0][1] + mat1[1][1] * mat2[1][1]) % 1000000
    return [[e00,e01],[e10,e11]]

def fibonacci_3(n):
    cur_mat = unit_mat
    ret_mat = [[1,0],[0,1]]
    while n > 0:
        if n%2:
            ret_mat = matmul22(ret_mat,cur_mat)
        n //= 2
        cur_mat = matmul22(cur_mat,cur_mat)
    return ret_mat[0][1]


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_3(n))
