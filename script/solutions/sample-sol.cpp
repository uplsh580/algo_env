// Ploblem: [평균은 넘겠지] https://www.acmicpc.net/problem/4344

// Solver: Seonghwna Lee
// Solved Date: 2021-03-06
// BigO: N

#include <iostream>
#include <vector>   // for vector       https://www.cplusplus.com/reference/vector/vector/
#include <numeric>  // for accumulate   https://www.cplusplus.com/reference/numeric/accumulate/
#include <math.h>   // for round        https://www.cplusplus.com/reference/cmath/?kw=math.h

using namespace std;

float solution(int N, vector<int> seq){
    int totalscore = accumulate(seq.begin(), seq.end(), 0);
    float avgscore = totalscore / N;
    int histudents = 0;
    
    for (vector<int>::iterator it = seq.begin(); it != seq.end(); it++)
        if (*it > avgscore) histudents ++;
    
    float ret = 100 * (float) histudents / N;

    return round(ret * 1000) / 1000;
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
