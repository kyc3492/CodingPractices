#include <iostream>
using namespace std;

int N, M;
char BOARD[11][11];
int ANS;

void MOVE(int direction, int COUNT, int R_loc[3], int B_loc[3]){
    if(COUNT > 10){
        if(ANS != -1){
            ANS = -1;
        }
        return;
    }

    if(direction == 0){
        COUNT++;
        cout << "moving UP\n";
        for(int i = 0; i < N; i++){
            if(BOARD[R_loc[0] + i][R_loc[1]] == '#'){
                cout << "WALL ENCOUNTERD!!\n";
                MOVE(2, COUNT);
                MOVE(3, COUNT);
            } else if(BOARD[R_loc[0] + i][R_loc[1]] == 'B'){
                cout << "BLUE BALL!!\n";
                if(ANS != -1){
                    ANS = -1;
                }
            } else if(BOARD[R_loc[0] + i][R_loc[1]] == 'O'){
                if(COUNT < ANS || ANS == -1){
                    ANS = COUNT;
                    cout << "ANS is " << ANS << "\n";
                }
            }
        }        
    }

    if(direction == 1){
        COUNT++;
        cout << "moving DOWN\n";
        for(int i = 0; i < N; i++){
            if(BOARD[R_loc[0] - i][R_loc[1]] == '#'){
                cout << "WALL ENCOUNTERD!!\n";
                MOVE(2, COUNT);
                MOVE(3, COUNT);
            } else if(BOARD[R_loc[0] + i][R_loc[1]] == 'B'){
                cout << "BLUE BALL!!\n";
                if(ANS != -1){
                    ANS = -1;
                }
            } else if(BOARD[R_loc[0] + i][R_loc[1]] == 'O'){
                if(COUNT < ANS || ANS == -1){
                    ANS = COUNT;
                    cout << "ANS is " << ANS << "\n";
                }
            }
        }        
    }

    if(direction == 2){
        COUNT++;
        cout << "moving LEFT\n";
        for(int i = 0; i < N; i++){
            if(BOARD[R_loc[0]][R_loc[1] - i] == '#'){
                cout << "WALL ENCOUNTERD!!\n";
                MOVE(0, COUNT);
                MOVE(1, COUNT);
            } else if(BOARD[R_loc[0] + i][R_loc[1]] == 'B'){
                cout << "BLUE BALL!!\n";
                if(ANS != -1){
                    ANS = -1;
                }
            } else if(BOARD[R_loc[0] + i][R_loc[1]] == 'O'){
                if(COUNT < ANS || ANS == -1){
                    ANS = COUNT;
                    cout << "ANS is " << ANS << "\n";
                }
            }
        }        
    }

    if(direction == 3){
        COUNT++;
        cout << "moving RIGHT\n";
        for(int i = 0; i < N; i++){
            if(BOARD[R_loc[0]][R_loc[1] + i] == '#'){
                cout << "WALL ENCOUNTERD!!\n";
                MOVE(0, COUNT);
                MOVE(1, COUNT);
            } else if(BOARD[R_loc[0] + i][R_loc[1]] == 'B'){
                cout << "BLUE BALL!!\n";
                if(ANS != -1){
                    ANS = -1;
                }
            } else if(BOARD[R_loc[0] + i][R_loc[1]] == 'O'){
                if(COUNT < ANS || ANS == -1){
                    ANS = COUNT;
                    cout << "ANS is " << ANS << "\n";
                }
            }
        }        
    }    
}

int main(void){
    int R_loc[3];
    int B_loc[3];

    cin >> N;
    cin >> M;

    for(int i = 0; i < N; i++){
        for(int j = 0; j < M; j++){
            cin >> BOARD[i][j];
            if (BOARD[i][j] == 'R'){
                R_loc[0] = i;
                R_loc[1] = j;
            }

            if (BOARD[i][j] == 'B'){
                B_loc[0] = i;
                B_loc[1] = j;
            }
        }
    }

    for(int i = 0; i < N; i++){
        for(int j = 0; j < M; j++){
            cout << BOARD[i][j];
        }
        cout << "\n";
    }

    MOVE(0, 0);
    MOVE(1, 0);
    MOVE(2, 0);
    MOVE(3, 0);
    cout << ANS;

}