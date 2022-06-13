#include <iostream>
#define SIZE 10000
using namespace std;

int main(){
	int T;
	cin >> T;
	
	for(int k = 0; k < T; k++){
		int N;
		int counter = 0;	
		cin >> N;
		
		if(N == 0){
			break;
		}
	
		//bool * arr = new bool[N + 1];
		bool arr[2 * SIZE + 1];
		for(int i = 0; i < 2 * SIZE + 1; i++){
			arr[i] = true;
		}
		//true: 소수, false: 소수아님
	
		arr[1] = true;
		for(int i = 2; i * i <= 2 * N; i++){
			if(arr[i] == true){			
				for(int j = 2; i * j <= 2 * N; j++){
					//cout << "Checking... " << i << " " << j << " " << i * j << endl;
					arr[i * j] = false;
				}
			}	
		}
		
		if(arr[N/2] == true){
			cout << N/2 << " " << N/2 << "\n";
		} else {
			for(int c = N/2; c > 1; --c){
				if(arr[c] == true && arr[N - c] == true){
					cout << c << " " << N - c << "\n";
					break;
				}
			}
		}
	}
		
	//delete []arr;
	return 0;
}