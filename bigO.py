import sys
import time
import argparse
import progressbar

parser = argparse.ArgumentParser(description='')
parser.add_argument('-n', default=1000000 ,dest='n', type=int, help='Number of Execution')
args = parser.parse_args()

def time_check(func):
    '''
    The decoration that checks the execution time.
    '''
    def wrapper(*args, **kwargs):
        print("-------------------------------------")
        print("FUNC NAME: {}".format(func.__name__))
        print("N: {}".format(args[0]))
        time_s = time.time()
        ret = func(*args, **kwargs)
        time_e = time.time()
        print("EXEC TIME: {}".format(time_e - time_s))
        print("-------------------------------------")
        print()
        return ret
    return wrapper

@time_check
def O_1(n):
    bar = progressbar.ProgressBar(maxval=n).start()
    ret = n * n
    bar.update(n)
    bar.finish()
    return ret

@time_check
def O_logN(n):
    bar = progressbar.ProgressBar(maxval=n).start()
    count = 0
    cur = n
    while cur > 1:
        cur /= 2
        count += 1
        bar.update(n-int(cur))
    bar.finish()
    return count

@time_check
def O_N(n):
    bar = progressbar.ProgressBar(maxval=n).start()
    ret = 0
    for i in range(n):
        ret += 1
        bar.update(i)
    bar.finish()
    return ret

@time_check
def O_NlogN(n):
    bar = progressbar.ProgressBar(maxval=n).start()
    count = 0
    for i in range(n):
        cur = i
        while cur > 1:
            cur /= 2
            count += 1
        bar.update(i)
    bar.finish()
    return count

@time_check
def O_NN(n):
    bar = progressbar.ProgressBar(maxval=n).start()
    ret = 0
    for i in range(n):
        for j in range(n): 
            ret += 1
        bar.update(i)
    bar.finish()
    return ret


if __name__ == '__main__':
    n = args.n

    O_1(n)
    time.sleep(1)

    O_logN(n)
    time.sleep(1)

    O_N(n)
    time.sleep(1)

    O_NlogN(n)
    time.sleep(1)

    O_NN(n)
