//https://www.acmicpc.net/problem/2292
#include <iostream>
using namespace std;

int main(){
	int N = 0, M = 6;
	int counter = 1;
	int cit = 1;
	
	cin >> N;
	
	for(counter; cit < N; counter++){
		cit += M * counter;
		//cout << cit << endl;
	}
	
	cout << counter << endl;
}