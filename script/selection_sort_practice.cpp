// Ploblem: [ATM] https://www.acmicpc.net/problem/11399
// [Required] Use the Selection Sort to solve it.

// Solver: 
// Solved Date: 
// BigO: 

#include <iostream>
#include <vector>

using namespace std;

void selection_sort(int n, vector<int> &seq){
    // TODO
}

int cal_total(vector<int> &seq){
    // TODO
    return 0;
}

int main(){
    int n;
    scanf("%d", &n);

    vector<int> seq;

    for (int i = 0; i < n; i++){
        int e;
        scanf("%d", &e);
        seq.push_back(e);
    }

    selection_sort(n, seq);
    printf("%d", cal_total(seq));

    return 0;
}
