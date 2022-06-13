//https://www.acmicpc.net/problem/2775
#include <iostream>
using namespace std;

int main(){
	int T = 0;
	int k, n;
	int total_apt[15][14] = {0};
	
	for(int i = 0; i < 15; i++){
		for(int j = 0; j < 14; j++){
			if(i == 0){
				total_apt[i][j] = j + 1;
			} else if(j == 0){
				total_apt[i][j] = 1;
			} else {
				total_apt[i][j] = total_apt[i - 1][j] + total_apt[i][j - 1];
			}
		}
	}
	/*
	for(int i = 0; i < 15; i++){
		for(int j = 0; j < 14; j++){
			cout << total_apt[i][j] << " ";
		}
		cout << endl;
	}
	*/

	cin >> T;
	
	for(int i = 0; i < T; i++){
		cin >> k;
		cin >> n;
		
		cout << total_apt[k][n - 1] << endl;
	}

}