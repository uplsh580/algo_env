// Ploblem: [ATM] https://www.acmicpc.net/problem/11399
// [Required] Use the Selection Sort to solve it.

// Solver: Seonghwan Lee
// Solved Date: 2021-03-07
// BigO: N^2

#include <iostream>
#include <vector>

using namespace std;

void selection_sort(int n, vector<int> &seq){
    for (int i = 0; i < n; i ++){
        int temp_min_pos = i;
        for (int j = i; j < n; j++) if (seq[temp_min_pos] > seq[j]) temp_min_pos = j;
        if (temp_min_pos != i) iter_swap(seq.begin() + i, seq.begin() + temp_min_pos);
    }
}

int cal_total(vector<int> &seq){
    int total_time = 0;
    int accumulate_time = 0;
    for (vector<int>::iterator it = seq.begin(); it < seq.end(); it++){
        accumulate_time += *it;
        total_time += accumulate_time;
    }

    return total_time;
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
