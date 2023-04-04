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
	int N;
	int counter = 0;
	cin >> N;
	
	for(int i = 0; i < N; i++){
		int num;
		cin >> num;
		
		if(num != 1 && Discriminator(num, num - 1) == false){
			counter++;
		}
	}
	cout << counter << endl;
}