#include <iostream>
using namespace std;

// 입력 받기 준비
// 배열은 4 x 4 x 2로 준비
int board[4][4][2] = {0};
// 반시계 방향으로 움직이는 배열 준비. 지시 방향에서 -1로 받아야한다.
int directions[8][2] = {{-1, 0}, {-1, -1}, {0, -1}, {1, -1}, {1, 0}, {1, 1}, {0, 1}, {-1, 1}};
int answer = 0;

void dfs(int board[][4][2], int current){
    // 최댓값 반영부터 진행
    if (current > answer){
        answer = current;
    }

    // 일단 물고기들을 다 움직이고 나서
    // 그렇게 해서 끝난 후 반영된 배열이 있을 거임.
    int after_board[4][4][2] = {0};
    // 배열을 일단 복사해준다.
    for (int c = 0; c < 4; c++){
        for (int r = 0; r < 4; r++){
            after_board[c][r][0] = board[c][r][0];
            after_board[c][r][1] = board[c][r][1];
        }
    }
    // 번호가 작은 물고기부터 이동한다.
    for (int fish = 1; fish < 17; fish++){
        // 움직였던 물고기의 중복 움직임을 방지
        bool isMoved = false;
        // 물고기 찾기
        for (int c = 0; c < 4; c++){
            // 이미 찾은 물고기면 탈출
            if (isMoved == true){
                break;
            }
            for (int r = 0; r < 4; r++){
                // 이미 찾은 물고기면 탈출
                if (isMoved == true){
                    break;
                }
                // 찾았으면 이동할거임
                if (after_board[c][r][0] == fish){
                    // 물고기 방향을 받아두고
                    int d = after_board[c][r][1] - 1;
                    // 8번의 방향 전환을 시도한다.
                    for (int idx = 0; idx < 8; idx++){
                        // 반시계 이동하다가 8을 넘어가면 -8로 복귀
                        if ((d + idx) >= 8){
                            d -= 8;
                        }
                        int dc = directions[d + idx][0];
                        int dr = directions[d + idx][1];
                        int nc = c + dc;
                        int nr = r + dr;
                        // board 내부에 있어야하고 상어(99)가 있으면 안된다.
                        if (0 <= nc && nc < 4 && 0 <= nr && nr < 4){
                            if (after_board[nc][nr][0] != 99){
                                // 이동이 가능하다면 서로 스왑하는 방식으로 진행.
                                // 또한 이동한 방향을 유지해야 하므로
                                after_board[c][r][1] = d + idx + 1;
                                int tmp_fish = after_board[c][r][0];
                                int tmp_d = after_board[c][r][1];
                                after_board[c][r][0] = after_board[nc][nr][0];
                                after_board[c][r][1] = after_board[nc][nr][1];
                                after_board[nc][nr][0] = tmp_fish;
                                after_board[nc][nr][1] = tmp_d;
                                isMoved = true;
                                break;
                            }
                        }
                    }
                }
            }
        }
    }

    // 상어를 찾는다. 상어는 99로 둘거임
    for (int c = 0; c < 4; c++){
        for (int r = 0; r < 4; r++){
            if (after_board[c][r][0] == 99){
                // 방향을 확인해줄 거임. -1 해야함에 유의
                int dc = directions[after_board[c][r][1] - 1][0];
                int dr = directions[after_board[c][r][1] - 1][1];

                // 움직일 수 있는 거리를 찾아줄 거임. 1 ~ 3의 범위가 될 것임.
                for (int dist = 1; dist < 4; dist++){
                    // 범위만큼 갔을 때 board 내라면 다음 단계로
                    // 또한 상어는 빈 칸으로 갈 수 없다.
                    int nc = c + (dc * dist);
                    int nr = r + (dr * dist);
                    if (0 <= nc && nc < 4 && 0 <= nr && nr < 4){
                        if (after_board[nc][nr][0] > 0){
                            // 상어가 물고기를 먹고
                            int eat = after_board[nc][nr][0];
                            int eat_d = after_board[nc][nr][1];
                            current += eat;
                            // 상어의 위치를 옮김.
                            after_board[nc][nr][0] = 99;
                            // 상어의 방향도 백업해 둠.
                            int shark_d = after_board[c][r][1];
                            // 현재 위치는 빈칸이 되게 함.
                            after_board[c][r][0] = 0;
                            after_board[c][r][1] = 0;
                            // 다음 단계를 다녀와서는
                            dfs(after_board, current);
                            // 롤백해줄거임. 먹은거 다시 살리고
                            after_board[nc][nr][0] = eat;
                            after_board[nc][nr][1] = eat_d;
                            // 상어 위치도 복귀
                            after_board[c][r][0] = 99;
                            // 상어의 방향도 다시 살려줌
                            after_board[c][r][1] = shark_d;
                            // 먹은거 뱉어내기
                            current -= eat;
                        }
                    }
                }
            }
        }
    }
}

int main(void){
    // 입력 받기

    for (int c = 0; c < 4; c++){
        for (int r = 0; r < 4; r++){
            cin >> board[c][r][0] >> board[c][r][1];
        }
    }

    // 상어의 출발은 (0, 0)에서 이므로
    int current = board[0][0][0];
    board[0][0][0] = 99;

    // 물고기들이 다 이동한 후 -> 상어가 이동해야함.
    dfs(board, current);
    cout << answer;
}