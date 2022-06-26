//https://www.acmicpc.net/problem/2869
#include <iostream>
using namespace std;

int main(){
	int A, B, V;
	int X;
	
	cin >> A >> B >> V;
	
	if((V - A) % (A - B) != 0){
		X = (V - A) / (A - B) + 1;
	} else {
		X = (V - A) / (A - B);
	}
	
	cout << X + 1 << endl;
}