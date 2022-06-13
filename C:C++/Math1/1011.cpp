#include <iostream>
using namespace std;

int main(){
	long T, x, y;
	long result;
	
	cin >> T;
	
	for(int i = 0; i < T; i++){
		cin >> x >> y;
		
		long standard = 0;
		long counter = 1;
		
		for(long j = 1; standard <= y - x; counter++){
			standard += j;
			if(counter == 1){
				//cout << counter << " " << j << " " << standard << endl;
				continue;			
			} else if(counter % 2 == 0){
				//cout << counter << " " << j << " " << standard << endl;
			} else {
				//cout << counter << " " << j << " " << standard << endl;
				j++;
			}
		}
		
		cout << counter - 2 << endl;
	}
	
	return 0;
}