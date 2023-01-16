// Ploblem: [피보나치 수 5] https://www.acmicpc.net/problem/10870

// Solver: Seonghwan Lee
// Solved Date: 2021-03-08
// BigO: 2^N

#include<iostream>
using namespace std;

int fib(int n){
    if (n == 0) return 0;
    else if (n == 1) return 1;
    else return fib(n-1) + fib(n-2);
}

int main(){
    int n;
    scanf("%d", &n);
    printf("%d", fib(n));
    return 0;
}
