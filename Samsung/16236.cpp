#include <iostream>
using namespace std;

int BOARD[21][21];
int MOVE_X[] = {0, 0, -1, 1};
int MOVE_Y[] = {-1, 1, 0, 0};

void DISTANCE(){
    
}

void SEARCHING(){
    
}

int main(void){
    int BABY_SHARK[3] = {0};
    int SHARK_SIZE = 2;
    int N;
    int TIME = 0;

    cin >> N;
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            cin >> BOARD[i][j];
            if(BOARD[i][j] == 9){
                BABY_SHARK[0] = i;
                BABY_SHARK[1] = j;
                BOARD[i][j] = 0;
            }
        }
    }

    cout << BABY_SHARK[0] << " " << BABY_SHARK[1] << "\n";
}