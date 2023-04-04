#include <iostream>
#define SIZE 100
using namespace std;

int main(){
	int N, M, tmp = 0, sum = 0;
	int nums[SIZE];
	cin >> N >> M;
	
	for(int i = 0; i < N; i++){
		cin >> nums[i];
	}
	
	for(int i = 0; i < N - 2; i++){
		for(int j = 1; i + j < N - 1; j++){
			for(int k = 1; i + j + k < N; k++){
				tmp = nums[i] + nums[i + j] + nums[i + j + k];
				//cout << i << " " << i + j << " " << i + j + k << " " << tmp << endl;
				if(tmp >= sum && tmp <= M){
					sum = tmp;
				}
			}
		}
	}
	
	cout << sum << endl;
	
	return 0;
}