#include <iostream>
using namespace std;

bool Discriminator(int num, int divitor){
	if(num % divitor == 0 && divitor > 1){
		//cout << num << " " << divitor << " true" << endl;
		return true;
	} else if(divitor <= 1) {
		//cout << num << " " << divitor << " false" << endl;
		return false;
	} else {
		//cout << num << " " << divitor << endl;
		return Discriminator(num, --divitor);
		
	}
}

int main(){
	int M, N;
	int sum = 0, first = -1;
	cin >> M;
	cin >> N;
	
	for(int i = N; i >= M; i--){
		if(i != 1 && Discriminator(i, i - 1) == false){
			first = i;
			sum += i;
		}
	}
	
	if(sum == 0 && first == -1){
		cout << first << endl;
	} else {
		cout << sum << endl;
		cout << first << endl;
	}
	
	return 0;
}