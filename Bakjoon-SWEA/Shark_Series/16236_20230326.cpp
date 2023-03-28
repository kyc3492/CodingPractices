#include <iostream>
#include <queue>
using namespace std;

// 초기값 설정
// 여차하면 전역변수로 때리기
int n = 0;
int shark_loc[2] = {0};
int shark_size = 2;
int ate = 0;
int answer = 0;
int board[21][21] = {0};
int dist_array[21][21];
int dc[4] = {-1, 1, 0, 0};
int dr[4] = {0, 0, -1, 1};

void bfs(){
    // 거리 기록용 배열
    for (int c = 0; c < n; c++){
        for (int r = 0; r < n; r++){
            dist_array[c][r] = {-1};
        }
    }

    // 큐 초기화. 현재 상어 위치를 먼저 넣어둔다.
    // 큐에다 넣을 때에는 pair로 쌍을 이루어준다.
    queue<pair<int, int>> q;
    q.push({shark_loc[0], shark_loc[1]});
    // 시작 전에 상어 위치의 거리는 0으로 바꾸고 시작한다.
    dist_array[shark_loc[0]][shark_loc[1]] = 0;

    while (!q.empty()){
        auto now = q.front();
        // pair의 접근은 first / second로 진행한다.
        int c = now.first;
        int r = now.second;
        // 가져온 것은 삭제해준다. pop과 같은 역할
        q.pop();
        // 각 방향으로 돌릴 것이다.
        for (int d = 0; d < 4; d++){
            int nc = c + dc[d];
            int nr = r + dr[d];
            // 다음 행선지가 범위 내인지를 확인한다.
            if (0 <= nc && nc < n && 0 <= nr && nr < n){
                // 범위 내라면 지나갈 수 있는지 + 한 번도 간적이 없는 곳인지 확인한다.
                if (board[nc][nr] <= shark_size and dist_array[nc][nr] == -1){
                    // 해당된다면 현재 위치에서 +1해서 다음 거리 적용해준다.
                    dist_array[nc][nr] = dist_array[c][r] + 1;
                    // 또한 다음 큐에 추가해준다.
                    // push에서는 놀랍게도 배열과 같은 형식이다.
                    q.push({nc, nr});
                }
            }
        }
    }

}

int find_prey(){
    // 거리 기록은 bfs로 구한다.
    bfs();

    // 상단, 좌측부터 시작해서 구한다. 이는 조건 중 상단 + 좌측을 우선시함을 반영.
    int next_shark_loc[2] = {0, 0};
    int current = n * n;

    for (int c = 0; c < n; c++){
        for (int r = 0; r < n; r++){
            // 거리가 -1 초과, 상어 크기 미만이어야함.
            // 또 실제로 먹이가 있어야함.
            if (dist_array[c][r] > -1 && dist_array[c][r] <= n * n && board[c][r] > 0 && board[c][r] < shark_size){
                // 거리가 더 작으면 바꾼다.
                if (current > dist_array[c][r]){
                    current = dist_array[c][r];
                    next_shark_loc[0] = c;
                    next_shark_loc[1] = r;
                }
            }
        }
    }
    // 거리 값에 변화가 없었다면
    if (current == n * n){
        return 0;
    // 거리 값에 변화가 있었다면
    } else {
        // 현재 상어의 위치를 0으로 초기화
        board[shark_loc[0]][shark_loc[1]] = 0;
        // 상어 위치는 옮겨준다.
        shark_loc[0] = next_shark_loc[0];
        shark_loc[1] = next_shark_loc[1];
        return current;
    }
}

int main(void){
    // 입력받기
    cin >> n;

    for (int c = 0; c < n; c++){
        for (int r = 0; r < n; r++){
            cin >> board[c][r];
            if (board[c][r] == 9){
                shark_loc[0] = c;
                shark_loc[1] = r;
            }
        }
    }

    while (1){
        // 먹이를 찾고난 후 결과 분석
        int current = find_prey();
        // 최근 찾아온 먹이가 없다면
        if (current == 0){
            // 정답출력
            cout << answer;
            break;
        } else {
            // 먹이가 있다면 answer에 더해주기
            answer += current;
            // 다음 상어 위치도 0으로 바꿔주고
            board[shark_loc[0]][shark_loc[1]] = 0;
            // 먹이를 먹었음을 반영
            ate++;
            // 만약 상어가 충분히 먹었다면 크기에 반영.
            if (shark_size == ate){
                shark_size++;
                ate = 0;
            }
        }
    }

    return 0;
}