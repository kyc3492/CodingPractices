#include <iostream>
#define MAX 9
using namespace std;
bool checker[MAX] = {false};
int answer[MAX];

void Searching(int index, int start, int N, int M){
	if(index == M){
		for(int i = 0; i < M; i++){
			cout << answer[i] << " ";
		}
		cout << "\n";
	}

	for(int i = start; i <= N; i++){
		if(checker[i] == false){
			answer[index] = i;
			checker[i] = true;
			Searching(index + 1, i, N, M);
			checker[i] = false;
		} else {
			continue;
		}
	}
}

int main(){
	int N, M;
	cin >> N >> M;
	
	Searching(0, 1, N, M);
	
	return 0;
}