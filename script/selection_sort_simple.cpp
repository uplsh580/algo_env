// Ploblem: [세수정렬] https://www.acmicpc.net/problem/2752
// [Required] Use the Selection Sort to solve it.

// Solver: 
// Solved Date: 
// BigO: 

#include <iostream>
#include <vector>

using namespace std;

void selection_sort(int n, vector<int> &seq){
    //TODO
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
