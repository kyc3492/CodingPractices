#include <iostream>
using namespace std;

int main(){
	int M, N, change = 64, tmp = 0, TOTALtmp = 0;
	char board[50][50];	
	char checker1[8][8] =
	{
		{'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
		{'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
		{'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
		{'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
		{'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
		{'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
		{'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
		{'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'}
	};	
	char checker2[8][8] =
	{
		{'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
		{'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
		{'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
		{'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
		{'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
		{'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
		{'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
		{'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'}
	};
	
	cin >> M >> N;
	
	for(int i = 0; i < M; i++){
		for(int j = 0; j < N; j++){
			cin >> board[i][j];
		}
	}
	
	for(int i = 0; i < M - 7; i++){
		for(int j = 0; j < N - 7; j++){
			tmp = 0;
			for(int k = 0; k < 8; k++){
				for(int l = 0; l < 8; l++){
					if(board[i + k][j + l] != checker1[k][l]){
						++tmp;
					}
					//cout << "(" << i + k << "," << j + l << ") / " << "(" << k << "," << l << ")\n";
					//cout << board[i + k][j + l] << " / " << checker1[k][l] << " " << tmp << "\n";
				}
			}
			if(change > tmp){
				change = tmp;
			}
		}
		//TOTALtmp += tmp;
	}
	
	for(int i = 0; i < M - 7; i++){
		for(int j = 0; j < N - 7; j++){
			tmp = 0;
			for(int k = 0; k < 8; k++){
				for(int l = 0; l < 8; l++){
					if(board[i + k][j + l] != checker2[k][l]){
						++tmp;
					}
					//cout << "(" << i + k << "," << j + l << ") / " << "(" << k << "," << l << ")\n";
					//cout << board[i + k][j + l] << " / " << checker2[k][l] << " " << tmp << "\n";
				}
			}
			if(change > tmp){
				change = tmp;
			}
		}
	}
	
	cout << change << endl;
}