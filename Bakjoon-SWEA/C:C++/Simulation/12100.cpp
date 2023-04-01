#include <iostream>
using namespace std;
const int MAX = 21;
int n = 0;

void DFS(int board[][MAX], int cnt){
    // 들어온 보드를 복사하면서
    // 4방향으로 90도 씩 시계 방향으로 돌거임.
    int rotated_board[MAX][MAX];
    for (int i = 0; i < 4; i++){
        for (int c = 0; c < n; c++){
            for (int r = 0; r < n; r++){
                rotated_board[r][n - c - 1] = board[c][r];
            }
        }

        // 돌린 배열을 바탕으로 숫자 합이 진행된 새로운 배열 생성.
        int after_board[MAX][MAX];
        for (int c = 0; c < n; c++){
            // 열을 하나씩 가져와서 작업할 거임.
            // 1. 돌면서 0이 있는지 파악. 있다면 0을 없애면서 오른쪽으로 붙여야 함.
            // idx -> after_board에 넣을 위치 / target -> rotated_board에서 확인 중인 위치
            int idx = n - 1;
            for (int target = n - 1; target > -1; target--){
                if (rotated_board[c][target] != 0){
                    after_board[c][idx] = rotated_board[c][target];
                    idx++;
                } else {
                    continue;
                }
            }
            // 2. 돌면서 합칠 수 있는게 있는지 파악
            // 한 번 합쳐진 것이 또 합쳐지지 않도록 주의. (4 2 2) -> (4 0 4) -> (0 4 4) -x-> (0 0 8)

        }

    }
}

int main(void){
    cin >> n;

    // 5번 돌려서 최대 값인걸 찾으려면 DFS인데
    // 배열의 맨 첫 포인터를 기준으로 넘기기 때문에
    // 배열은 정해져있는 상수값으로 이어져있어야 함.
    int board[MAX][MAX];

    DFS(board, 0);

}