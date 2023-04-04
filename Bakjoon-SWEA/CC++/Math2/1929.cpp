#include <iostream>
#define SIZE 1000000
using namespace std;

int main(){
	int M, N;	
	cin >> M >> N;
	
	//bool * arr = new bool[N + 1];
	bool arr[SIZE + 1];
	for(int i = 0; i < SIZE + 1; i++){
		arr[i] = true;
	}
	//true: 소수, false: 소수아님
	
	arr[1] = true;
	for(int i = 2; i * i <= SIZE; i++){
		if(arr[i] == true){			
			for(int j = 2; i * j <= SIZE; j++){
				//cout << "Checking... " << i << " " << j << " " << i * j << endl;
				arr[i * j] = false;
			}
		}	
	}
		
	for(int i = M; i <= N; i++){
		if(arr[i] == true && i != 1){
			cout << i << "\n";
		}
	}
	
	//delete []arr;
	return 0;
}