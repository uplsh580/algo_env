// Ploblem: [평균은 넘겠지] https://www.acmicpc.net/problem/4344

// Solver: 
// Solved Date: 
// BigO:

#include <iostream>
#include <vector>
#include <string>
using namespace std;

float solution(int N, vector<int> seq){
    return 0;
}

int main(){
    int C;
    scanf("%d", &C);

    for(int i = 0; i < C; i++){
        int N;
        scanf("%d", &N);

        vector<int> seq;
        int cur_e;
        for(int j = 0; j < N; j++){
            scanf("%d", &cur_e);
            seq.push_back(cur_e);
        }

        printf("%.3lf %% \n", solution(N, seq));
    }
    return 0;
}
