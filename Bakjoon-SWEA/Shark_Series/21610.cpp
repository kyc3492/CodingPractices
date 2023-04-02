#include <iostream>
using namespace std;

int main(void){
    int n, m = 0;
    cin >> n >> m;

    int area[n][n];
    for (int c = 0; c < n; c++){
        for (int r = 0; r < n; r++){
            cin >> area[c][r];
        }
    }

    int moves[m][2];
    for (int idx = 0; idx < m; idx++){
        cin >> moves[idx][0] >> moves[idx][1];
    }

    // 이동 방향을 저장한다.
    int dc[8] = {0, -1, -1, -1, 0, 1, 1, 1};
    int dr[8] = {-1, -1, 0, 1, 1, 1, 0, -1};

    // 구름 정보를 담을 배열
    int clouds[n][n];
    for (int c = 0; c < n; c++){
        for (int r = 0; r < n; r++){
            clouds[c][r] = 0;
        }
    }
    // 최초 구름 생성
    clouds[n - 1][0] = 1;
    clouds[n - 1][1] = 1;
    clouds[n - 2][0] = 1;
    clouds[n - 2][1] = 1;

    // 움직임을 구현한다. 입력 받은 움직임들 idx를 돈다.
    for (int idx = 0; idx < m; idx++){
        int now_dc = dc[moves[idx][0] - 1];
        int now_dr = dr[moves[idx][0] - 1];
        int now_s = moves[idx][1];
        // s가 범위보다 크게 들어오는 경우가 있음. 이를 해결.
        now_s = now_s % n;
        int now_clouds[n][n];
        for (int c = 0; c < n; c++){
            for (int r = 0; r < n; r++){
                now_clouds[c][r] = 0;
            }
        }

        // 맘 편하게 구름 배열 자체를 옮겨버리자.
        for (int c = 0; c < n; c++){
            for (int r = 0; r < n; r++){
                // 다음 위치를 보는데
                int nc = c + (now_dc * now_s);
                int nr = r + (now_dr * now_s);
                // 다음 위치가 음수거나 n을 넘어가는지 확인.
                if (nc >= n){
                    nc -= n;
                }
                if (nc < 0){
                    nc += n;
                }
                if (nr >= n){
                    nr -= n;
                }
                if (nr < 0){
                    nr += n;
                }
                // 다음 구름으로 이동.
                now_clouds[nc][nr] = clouds[c][r];
            }
        }

        // 새로운 구름을 갱신
        for (int c = 0; c < n; c++){
            for (int r = 0; r < n; r++){
                clouds[c][r] = now_clouds[c][r];
                // 해당 지역에 구름이 생긴다면
                if (clouds[c][r] == 1){
                    // 비를 1 내린다. 구름은 나중에 새로운 구름을 생성할 때 삭제.
                    area[c][r] += 1;
                }                
            }
        }

        // 바구니를 확인하며 대각선들에 물이 있는지 확인.
        for (int c = 0; c < n; c++){
            for (int r = 0; r < n; r++){
                // 비구름에 해당되면.
                if (clouds[c][r] > 0){
                    int water = 0;
                    // 방향 배열 상 1, 3, 5, 7
                    for (int dir = 1; dir < 8; dir += 2){
                        int nc = c + dc[dir];
                        int nr = r + dr[dir];
                        // 범위를 넘어가는 지 확인.
                        if (0 <= nc && nc < n && 0 <= nr && nr < n){
                            // 해당 대각선에 물이 있는가?
                            if (area[nc][nr] > 0){
                                water++;
                            }
                        }
                    }
                    area[c][r] += water;
                }
            }
        }

        // 새로운 구름의 생성.
        for (int c = 0; c < n; c++){
            for (int r = 0; r < n; r++){
                // 전에 구름이 없었고 + 현재 물이 2이상이어야 함.
                if (clouds[c][r] == 0 && area[c][r] >= 2){
                    // 구름 생성
                    clouds[c][r] = 1;
                    // 물 2 증발
                    area[c][r] -= 2;
                }
                // 구름 있었던 곳은 삭제.
                else if (clouds[c][r] == 1){
                    clouds[c][r] = 0;
                }
            }
        }
    }
    // 전체 총합 구하기
    int answer = 0;
    for (int c = 0; c < n; c++){
        for (int r = 0; r < n; r++){
            answer += area[c][r];
        }
    }
    cout << answer;

    return 0;
}