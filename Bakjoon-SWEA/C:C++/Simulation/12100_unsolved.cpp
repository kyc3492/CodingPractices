#include <iostream>
using namespace std;
const int MAX = 21;
int n = 0;
int answer = 0;

void DFS(int board[][MAX], int cnt){
    // 카운트가 5에 도달했다면 최댓값을 찾아본다.
    if (cnt == 5){
        return;
    }

    // 최댓값 찾아주기.
    int current = 0;
    for (int c = 0; c < n; c++){
        for (int r = 0; r < n; r++){
            if (current < board[c][r]){
                current = board[c][r];
            }
        }
    }
    if (answer < current){
        answer = current;
    }

    // 들어온 보드를 복사하면서
    // 4방향으로 90도 씩 시계 방향으로 돌거임.
    int rotated_board[MAX][MAX];
    for (int c = 0; c < MAX; c++){
        for (int r = 0; r < MAX; r++){
            rotated_board[c][r] = 0;
        }
    }
    for (int i = 0; i < 4; i++){
        for (int c = 0; c < n; c++){
            for (int r = 0; r < n; r++){
                rotated_board[r][n - c - 1] = board[c][r];
            }
        }

        // 돌린 배열을 바탕으로 숫자 합이 진행된 새로운 배열 생성.
        int after_board[MAX][MAX];
        for (int c = 0; c < MAX; c++){
            for (int r = 0; r < MAX; r++){
                after_board[c][r] = 0;
            }
        }
        for (int c = 0; c < n; c++){
            // 열을 하나씩 가져와서 작업할 거임.
            // 1. 돌면서 0이 있는지 파악. 있다면 0을 없애면서 오른쪽으로 붙여야 함.
            // idx -> after_board에 넣을 위치 / target -> rotated_board에서 확인 중인 위치
            int idx = n - 1;
            for (int target = n - 1; target > -1; target--){
                if (rotated_board[c][target] != 0){
                    after_board[c][idx] = rotated_board[c][target];
                    idx--;
                } else {
                    continue;
                }
            }
            // 2. 돌면서 합칠 수 있는게 있는지 파악
            // 한 번 합쳐진 것이 또 합쳐지지 않도록 주의. (4 2 2) -> (4 0 4) -> (0 4 4) -x-> (0 0 8)
            for (int idx = n - 1; idx > 0; idx--){
                // idx와 idx - 1이 같다면 idx 위치로 더한다. 0이 아님을 체크
                if (after_board[c][idx] == after_board[c][idx - 1] && after_board[c][idx] != 0){
                    after_board[c][idx] = after_board[c][idx] * 2;
                    after_board[c][idx - 1] = 0;
                }
            }
            // 3. 0을 지우며 오른쪽 정렬 진행.
            for (int target = n - 1; target > -1; target--){
                // target이 빈칸이라면
                if (after_board[c][target] == 0){
                    // idx가 가져올 수 있는 다른 수인 지 확인
                    for (int idx = target - 1; idx > -1; idx--){
                        // 0이 아닌 다른 수가 있다면 가져온다.
                        if (after_board[c][idx] > 0){
                            after_board[c][target] = after_board[c][idx];
                            after_board[c][idx] = 0;
                        }
                    }
                }
            }
        }
        // 4. 진행된 배열로 다음 DFS를 돌게 한다.
        DFS(after_board, cnt + 1);
    }
}

int main(void){
    cin >> n;

    // 5번 돌려서 최대 값인걸 찾으려면 DFS인데
    // 배열의 맨 첫 포인터를 기준으로 넘기기 때문에
    // 배열은 정해져있는 상수값으로 이어져있어야 함.
    int board[MAX][MAX];
    for (int c = 0; c < MAX; c++){
        for (int r = 0; r < MAX; r++){
            board[c][r] = 0;
        }
    }
    for (int c = 0; c < n; c++){
        for (int r = 0; r < n; r++){
            cin >> board[c][r];
        }
    }
    

    DFS(board, 0);
    cout << answer;
}