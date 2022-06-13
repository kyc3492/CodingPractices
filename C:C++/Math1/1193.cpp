//https://www.acmicpc.net/problem/1193
#include <iostream>
using namespace std;

int main(){
	int N = 0, sum = 0;
	int numerator, denumerator;
	cin >> N;
	
	for(int i = 1; sum < N; i++){
		sum += i;
		
		if(i % 2 != 0){
			denumerator = i - (sum - N);
			numerator = i - denumerator + 1;
		} else {
			numerator = i - (sum - N);
			denumerator = i - numerator + 1;
		}	
	}
	
	cout << numerator << "/" << denumerator << endl;
}