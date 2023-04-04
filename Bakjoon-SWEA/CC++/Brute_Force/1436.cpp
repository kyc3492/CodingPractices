#include <iostream>
#include <cmath>
using namespace std;

int main(){
	int N, count = 1, num = 0;
	
	cin >> N;
	
	if(N == 1){
		num = 666;
	} else {
		for(int i = 666; i > 0; i++){
		//cout << "init... " << i << "\n";
			for(int c = 1; pow(10, c + 1) <= i; c++){
				//cout << "inner...  " << c << "\n";
				if(int(i / pow(10, c - 1)) - (int((i / pow(10, c))) * 10) == 6){
					//cout << int(i / pow(10, c - 1)) - (int((i / pow(10, c))) * 10) << '\n';
					if(int(i / pow(10, c)) - (int((i / pow(10, c + 1))) * 10) == 6){
						//cout << int(i / pow(10, c)) - (int((i / pow(10, c + 1))) * 10) << '\n';
						if(int(i / pow(10, c + 1)) - (int((i / pow(10, c + 2))) * 10) == 6){
								//cout << int(i / pow(10, c + 1)) - (int((i / pow(10, c + 2))) * 10) << '\n';
								count++;
								//cout << count << " " << i << '\n';
								break;
						}
					}
				}
			}
			if(N == count - 1){
				num = i;
				break;
			}
		}
	}
	
	cout << num;
}