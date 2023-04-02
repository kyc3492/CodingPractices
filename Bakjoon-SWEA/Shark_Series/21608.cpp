#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int main(void){
    int n = 0;
    cin >> n;
    int like_table[n * n][4];

    int dc[4] = {-1, 1, 0, 0};
    int dr[4] = {0, 0, -1, 1};

    int classroom[n][n];
    for (int c = 0; c < n; c++){
        for (int r = 0; r < n; r++){
            classroom[c][r] = 0;
        }
    }

    for (int idx = 0; idx < n * n; idx++){
        int student;
        int likes[4] = {0,};
        vector<pair<int, int>> candi;

        cin >> student;
        for (int i = 0; i < 4; i++){
            cin >> likes[i];
            like_table[student - 1][i] = likes[i];
        }

        // 1. 비어있는 칸 중 좋아하는 학생이 인접한 칸이 가장 많은 칸.
        int like_classroom[n][n];
        for (int c = 0; c < n; c++){
            for (int r = 0; r < n; r++){
                like_classroom[c][r] = 0;
            }
        }
        int max_ple = 0;
        for (int c = 0; c < n; c++){
            for (int r = 0; r < n; r++){
                // 비어있다면,
                if (classroom[c][r] == 0){
                    // 주변 탐색.
                    for (int d = 0; d < 4; d++){
                        int nc = c + dc[d];
                        int nr = r + dr[d];
                        // 다음 탐색 자리가 범위 내 인가?
                        if (0 <= nc && nc < n && 0 <= nr && nr < n){
                            for (int s = 0; s < 4; s++){
                                // 옆자리가 좋아하는 학생인가?
                                if (classroom[nc][nr] == likes[s]){
                                    // 만족도 + 1
                                    like_classroom[c][r]++;
                                }
                            }
                        }
                    }
                }
                if (like_classroom[c][r] > max_ple){
                    max_ple = like_classroom[c][r];
                }
            }
        }
        // 1번 자리들 중 만족도가 높은 자리들을 체크해야 한다.
        for (int c = 0; c < n; c++){
            for (int r = 0; r < n; r++){
                if (like_classroom[c][r] == max_ple && classroom[c][r] == 0){
                    candi.push_back({c, r});
                }
            }
        }
        // 여러개인지 파악, 후보군이 하나라면 자리 배치
        if (candi.size() == 1){
            auto seat = candi.front();
            classroom[seat.first][seat.second] = student;
            continue;
        }

        // 2. 인접한 칸 중 비어있는 칸이 가장 많은 곳 파악
        int max_empties = 0;
        int array_empties[candi.size()] = {0,};
        for (int e = 0; e < candi.size(); e++){
            auto seat = candi[e];
            int c = seat.first;
            int r = seat.second;

            // 주변의 빈 자리들 파악
            int empties = 0;
            // 4방향 탐색
            for (int d = 0; d < 4; d++){
                int nc = c + dc[d];
                int nr = r + dr[d];
                if (0 <= nc && nc < n && 0 <= nr && nr < n){
                    if (classroom[nc][nr] == 0){
                        empties++;
                    }
                }
            }
            array_empties[e] = empties;
            if (max_empties < empties){
                max_empties = empties;
            }
        }
        // 빈 칸이 적은 자리들을 쳐냄. (21, 21)로 처리함으로써 후보에서 제외시킹.
        for (int e = 0; e < candi.size(); e++){
            if (array_empties[e] < max_empties){
                candi[e] = {21, 21};
            }
        }

        // 바로 3번으로. 상단, 좌측 칸을 찾는다.
        sort(candi.begin(), candi.end());
        auto seat = candi.front();
        classroom[seat.first][seat.second] = student;
    }

    int answer = 0;
    // 만족도 계산
    for (int c = 0; c < n; c++){
        for (int r = 0; r < n; r++){
            int now_likes = 0;
            // 4방향 확인
            for (int d = 0; d < 4; d++){
                int nc = c + dc[d];
                int nr = r + dr[d];
                if (0 <= nc && nc < n && 0 <= nr && nr < n){
                    for (int s = 0; s < 4; s++){
                        // 앉아있는 학생 기준 옆자리가 좋아하는 학생인가?
                        if (classroom[nc][nr] == like_table[classroom[c][r] - 1][s]){
                            // 만족도 + 1
                            now_likes++;
                        }
                    }
                }
            }
            // 파악이 끝났다면 답에 더해줌.
            if (now_likes < 1){
                continue;
            } else {
                answer += pow(10, now_likes - 1);
            }
        }
    }
    cout << answer;
    return 0;
}