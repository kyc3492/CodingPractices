#include <iostream>
#include <cmath>
using namespace std;

int main(){
	int N, tmp, M = 0;
	
	cin >> N;
	tmp = 0;
	
	for(int i = 0; i < N; i++){
		tmp = i;
		for(int j = 0; pow(10, j) < i; j++){
			tmp += int(i / pow(10, j)) - (int(((i / pow(10, j + 1)))) * 10);
		}
		if(N == tmp){
			M = i;
			break;
		}
	}
	
	cout << M << endl;
}