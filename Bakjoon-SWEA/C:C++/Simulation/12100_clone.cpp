// 도저히 답답해서 na982 님 설명듣고 클론 코딩 중...

#include <iostream>
using namespace std;

int n;
int answer;

// 구조체 개념 확실히 할 것.
struct BOARD
{
    int board[20][20];

    // 90도 시계방향으로 돌리는 함수
    void rotate() {
        int temp[20][20];

        // 돌린 보드를 임시저장하고
        for (int c = 0; c < n; c++){
            for (int r = 0; r < n; r++){
                temp[c][r] = board[n - r - 1][c];
            }
        }

        // 다시 원래 보드로 저장
        for (int c = 0; c < n; c++){
            for (int r = 0; r < n; r++){
                board[c][r] = temp[c][r];
            }
        }
    }

    // 현재 단계에서 가장 큰 값을 구하는 함수
    int get_max(){
        int current = 0;

        for (int c = 0; c < n; c++){
            for (int r = 0; r < n; r++){
                if (current < board[c][r]){
                    current = board[c][r];
                }
            }
        }
        return current;
    }

    // 위로 합치면서 올리는 함수.
    void up(){
        int temp[20][20];

        for (int r = 0; r < n; r++){
            // 직전에 갱신이 있었는지를 파악하는 변수.
            // 이를 활용해 갱신 이후에 오는 같은 수에도 더하지 않도록 해준다.
            bool canUpdate = false;
            // temp 위 위치를 가르킬 변수. 보드의 c보다 항상 이전 값이어야 바람직하다.
            // 때문에 -1로 시작하고 전위로 ++target을 해준다.
            int target = -1;
            for (int c = 0; c < n; c++){
                // 보드에 빈 칸이면 넘어간다.
                if (board[c][r] == 0){
                    continue;
                }
                // 보드의 값과 temp의 target 값이 같다면 + 갱신 가능한 상황이라면
                if (board[c][r] == temp[target][r] && canUpdate == true){
                    temp[target][r] *= 2;
                    canUpdate = false;
                }
                // 나머지 상황에서는 새로운 값을 temp에 추가한다.
                else {
                    temp[++target][r] = board[c][r];
                    canUpdate = true;
                }
            }
            // 돌고 난 후 0으로 채우기. 쓰레기 값 방지
            for (++ target; target < n; ++target){
                temp[target][r] = 0;
            }
        }

        // 다시 원래 보드로 저장
        for (int c = 0; c < n; c++){
            for (int r = 0; r < n; r++){
                board[c][r] = temp[c][r];
            }
        }
    }
};

void dfs(BOARD cur_board, int cnt){
    // 5번째 횟수에 도달했다면 이 때까지의 최댓값을 불러와 전역 answer 변수와 비교.
    if (cnt == 5){
        int current = cur_board.get_max();
        if (answer < current){
            answer = current;
        }
        return;
    }

    // 아니라면 4방향 돌기.
    for (int dir = 0; dir < 4; dir++){
        // 현재 보드를 next에 복사
        BOARD next = cur_board;
        // 복사된 next에서 up 수행.
        next.up();
        // 복사된 next를 다음 깊이로 넘김
        dfs(next, cnt + 1);
        // 끝내고 왔다면 현재의 보드를 돌리기.
        cur_board.rotate(); 
    }
}

int main(void){
    BOARD board;
    cin >> n;

    for (int c = 0; c < n; c++){
        for (int r = 0; r < n; r++){
            cin >> board.board[c][r];
        }
    }

    answer = 0;
    dfs(board, 0);
    cout << answer;

    return 0;
}