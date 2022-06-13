#include <iostream>
using namespace std;

int main(){
	int N, x, y;
	int people[50][2];
	int rank[50];
	
	cin >> N;
	for(int i = 0; i < N; i++){
		cin >> people[i][0] >> people[i][1];
		rank[i] = 1;
	}
	
	for(int i = 0; i < N - 1; i++){
		for(int j = i + 1; j < N; j++){
			if(people[i][0] > people[j][0] && people[i][1] > people[j][1]){
				rank[j]++;
			} else if(people[i][0] < people[j][0] && people[i][1] < people[j][1]) {
				rank[i]++;
			}
			//cout << people[i][0] << " " << people[i][1] << " / " << people[j][0] << " " << people[j][1] << "\n";
		}
	}
	
	for(int i = 0; i < N; i++){
		cout << rank[i] << " ";
	}
}