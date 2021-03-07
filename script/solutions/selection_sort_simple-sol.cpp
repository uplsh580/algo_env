// Ploblem: [세수정렬] https://www.acmicpc.net/problem/2752
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

int main(){
    vector<int> seq;

    for (int i = 0; i < 3; i++){
        int e;
        scanf("%d", &e);
        seq.push_back(e);
    }

    selection_sort(3, seq);

    for (int i = 0; i < 3; i++){
        printf("%d ", seq[i]);
    }
    return 0;
}
