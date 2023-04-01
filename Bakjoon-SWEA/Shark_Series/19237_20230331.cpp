#include <iostream>
using namespace std;

int main(void){
    int n, m, k = 0;
    cin >> n >> m >> k;

    // 입력할 대 한 칸에 3개의 정보가 들어갈 것임
    // {상어 번호, 남은 냄새}
    // 비어있다면 {0, 0}
    int bowl[n][n][2];
    // 상어가 바라보는 방향은 bowl에 반영 안하고 따로 배열을 만들어 줄 것임.
    // 굳이 루프를 도는 것도 방지하고 지나치게 메모리를 많이 먹기도 하니까.
    int shark_head[m] = {0};
    // 상어의 존재 여부를 체크하는 배열을 생성해줌.
    bool isSharkHere[m];
    for (int idx = 0; idx < m; idx++){
        isSharkHere[idx] = true;
    }
    // 방향에 대한 배열. idx + 1이 입력된 방향임.
    // 위: 0, 아래: 1, 왼쪽: 2, 오른쪽: 3
    int directions[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    // 상어 정보 입력 받기
    for (int c = 0; c < n; c++){
        for (int r = 0; r < n; r++){
            cin >> bowl[c][r][0];
            // 상어가 들어온거라면 냄새는 k로 초기화
            if (bowl[c][r][0] > 0){
                bowl[c][r][1] = k;
            // 아니라면 냄새도 0. 쓰레기값이 들어오더라.
            } else {
                bowl[c][r][1] = 0;
            }
        }
    }

    // 상어가 처음에 바라보는 방향 기록
    // 기록할 때부터 -1을 해버리자.
    for (int idx = 0; idx < m; idx++){
        int tmp;
        cin >> tmp;
        shark_head[idx] = tmp - 1;
    }

    // 상어의 움직임 테이블도 기록해줄 거임.
    // 상어 idx에 맞추려면 0으로 빈 상어 칸을 하나 만들고 기록하자.
    int priority_table[m + 1][4][4] = {0};
    for (int shark = 1; shark < m + 1; shark++){
        // 방향은 이미 -1 씩 해줬으니 그대로 입력해도 됨.
        // 단 입력되는 값도 -1 이어야함.
        for (int head = 0; head < 4; head++){
            for (int next_move = 0; next_move < 4; next_move++){
                int tmp;
                cin >> tmp;
                priority_table[shark][head][next_move] = tmp - 1;
            }
        }
    }

    int answer = 0;
    // 이제 상어가 움직인다. 번호가 큰 놈부터 움직이다가 1만이 남을 때까지.
    while (1){
        // 움직이기 이전의 배열을 복사해둔다.
        int bowl_prev[n][n][2];
        for (int c = 0; c < n; c++){
            for (int r = 0; r < n; r++){
                bowl_prev[c][r][0] = bowl[c][r][0];
                bowl_prev[c][r][1] = bowl[c][r][1];
            }
        }

        // 경과한 시간이 1000초를 넘어가면 -1을 출력하도록 함.
        if (answer > 1000){
            answer = -1;
            break;
        }

        // 또한 상어가 1만 남았는지 확인한다.
        int noShark = 0;
        for (int idx = 1; idx < m; idx++){
            if (isSharkHere[idx] == false){
                noShark++;
            }
        }
        if (noShark == m - 1){
            break;
        }

        for (int shark = m; shark > 0; shark--){
            // 현재 체크 중인 상어가 존재 하는지 확인한다.
            if (isSharkHere[shark - 1] == false){
                continue;
            }
            // 현재 번호의 상어를 찾는다. 현재 위치에 있다면 냄새도 k여야한다.
            // 지금의 상어가 이미 이동을 마쳤는가?
            bool isMoved = false;
            for (int c = 0; c < n; c++){
                if (isMoved == true){
                    break;
                }
                for (int r = 0; r < n; r++){
                    if (isMoved == true){
                        break;
                    }
                    if (bowl[c][r][0] == shark && bowl[c][r][1] == k){
                        // 찾았으면 현재 바라보는 방향을 체크
                        int now_head = shark_head[shark - 1];
                        // 바라보는 방향에 따른 방향 우선순위 가져오기
                        int move_priority[4] = {0};
                        for (int i = 0; i < 4; i++){
                            move_priority[i] = priority_table[shark][now_head][i];
                        }
                        // 우선순위 배열을 돌면서 이동할 수 있는지 체크
                        // 이동 가능 우선 순위는 1. 빈 칸인가 /  2. 내가 왔던 길인가.
                        // 이동 못하는 경우는 없음. 내가 있던 데로 가면 되니까.
                        // 그러나 만약, 직전에 빈 칸이었고 + 다른 큰 번호의 상어가 있다면 그 칸으로는 이동 가능.
                        for (int d = 0; d < 4; d++){
                            int dc = directions[move_priority[d]][0];
                            int dr = directions[move_priority[d]][1];
                            int nc = c + dc;
                            int nr = r + dr;
                            // 내부인지 체크
                            if (0 <= nc && nc < n && 0 <= nr && nr < n){
                                // 직전에 빈 칸이었나?
                                if (bowl_prev[nc][nr][1] == 0){
                                    // 빈 칸이었어서 이동하려 보니 이미 다른 상어가 와 있는가?
                                    if (bowl[nc][nr][0] > shark && bowl[nc][nr][1] == k + 1){
                                        // 상어 내쫒은거 반영
                                        isSharkHere[bowl[nc][nr][0] - 1] = false;
                                    }
                                    // 가능하므로 이동.
                                    bowl[nc][nr][0] = shark;
                                    // 전체 이동이 끝난 후 냄새를 1씩 빼줄 것을 고려.
                                    bowl[nc][nr][1] = k + 1;
                                    isMoved = true;
                                    // 상어의 현재 바라보는 위치를 반영.
                                    shark_head[shark - 1] = move_priority[d];
                                    break;
                                }
                            }
                        }
                        // 차선책. 위에서 움직임이 없었다면 내 냄새가 있는 곳으로 돌아간다.
                        if (isMoved == false){
                            for (int d = 0; d < 4; d++){
                                int dc = directions[move_priority[d]][0];
                                int dr = directions[move_priority[d]][1];
                                int nc = c + dc;
                                int nr = r + dr;
                                // 내부인지 체크
                                if (0 <= nc && nc < n && 0 <= nr && nr < n){
                                    // 내가 돌아온 길인가?
                                    if (bowl_prev[nc][nr][0] == shark){
                                        bowl[nc][nr][0] = shark;
                                        bowl[nc][nr][1] = k + 1;
                                        // 상어의 현재 바라보는 위치를 반영.
                                        shark_head[shark - 1] = move_priority[d];
                                        break;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        // 남아있는 다른 냄새들 after로 반영. 현재 냄새에서 1 빼서 반영해준다.
        for (int c = 0; c < n; c++){
            for (int r = 0; r < n; r++){
                // 냄새가 있다면 뺀다. 단, 상어 본체가 있으면 제외해야함.
                if (bowl[c][r][1] > 0){
                    bowl[c][r][1]--;
                    if (bowl[c][r][1] == 0){
                        bowl[c][r][0] = 0;
                    }
                }
            }
        }
        answer++;
    }

    cout << answer;
    return 0;
}