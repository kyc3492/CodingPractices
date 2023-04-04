#include <iostream>
using namespace std;

int main(){
	while(1){
		int a, b, c, tmp;
		
		cin >> a >> b >> c;
		
		if(a == 0 && b == 0 && c == 0){
			break;
		}
		
		if(a < b){
			tmp = a;
			a = b;
			b = tmp;
		}
		if(a < c){
			tmp = a;
			a = c;
			c = tmp;
		}
		if(b < c){
			tmp = b;
			b = c;
			c = tmp;
		}
		
		if(a*a == b*b + c*c){
			cout << "right" << endl;
		} else {
			cout << "wrong" << endl;
		}
	}
	
	return 0;
}