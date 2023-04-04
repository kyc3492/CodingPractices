//https://www.acmicpc.net/problem/10250
#include <iostream>
using namespace std;

int main(){
	int T, H, W, N;
	int floor, number;
	
	cin >> T;
	
	for(int i = 0; i < T; i++){
		cin >> H >> W >> N;
		number = (N / H) + 1;
		floor = N % H;
		if(floor == 0){
			floor = H;
			number -= 1;
		}
		cout << (floor * 100) + number << endl;
	}
}