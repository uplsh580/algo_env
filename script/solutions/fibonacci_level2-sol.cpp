// Ploblem: [피보나치 수 4] https://www.acmicpc.net/problem/10826

// Solver: Seonghwan Lee
// Solved Date: 2021-03-08
// BigO: N

#include<iostream>
using namespace std;

unsigned long long fib(int n){
    unsigned long long arr[n+1];
    arr[0] = 0;
    arr[1] = 1;

    for (int i = 2; i < n+1; i++){
        arr[i] = arr[i-1] + arr[i-2];
    }
    return arr[n];
}

int main(){
    int n;
    scanf("%d", &n);
    printf("%llu", fib(n));
    return 0;
}
