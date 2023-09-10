#include <iostream>
using namespace std;

string BW[8] = {
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB"
};

string WB[8] = {
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW"
};

string arr[50];
int BW_cnt(int x, int y){
    int cnt = 0; //초기화 필요
    for(int i=0; i<8; i++){
        for(int j=0; j<8; j++){
            if(arr[x+i][y+j]!= BW[i][j]){
                cnt++;
            }
        }
    }
    return cnt;
}
int WB_cnt(int x, int y){
    int cnt = 0; //초기화 필요
    for(int i=0; i<8; i++){
        for(int j=0; j<8; j++){
            if(arr[x+i][y+j] != WB[i][j]){
                cnt++;
            }
        }
    }
    return cnt;
}

int main(){
    int m, n;
    
    cin >> m >> n; 


    for(int i=0; i<m; i++){
        cin >> arr[i];
    }
    
    int r_min = 10000; //min값 초기화
    for(int i=0; i+8<=m; i++){
        for(int j=0; j+8<=n; j++){
            int tmp;
            tmp=min(BW_cnt(i,j),WB_cnt(i,j));
            if(tmp < r_min){
                r_min = tmp;
            }
        }
    
    }

    cout << r_min;

    return 0;
}