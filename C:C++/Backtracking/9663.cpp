#include <iostream>
#define MAX 15
using namespace std;

int X[MAX] = {MAX};
int Y[MAX] = {MAX};
int counter = 0;

void Searching(int N, int index){
    if(index == N + 1){
        cout << index << " finished!\n";
        counter++;
    } else {
        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                cout << index << " / " << i << ", " << j <<"\n";
                X[index] = i;
                Y[index] = j;
                if(index != 0){
                    for(int k = 0; k <= index; k++){
                        cout << "init?\n";
                        if(X[k] == i || Y[k] == j || Y[k] == i || Y[k] == 14 - i){
                            cout << X[k] << ", " << Y[k] <<"\n";
                            cout << "PASS\n";
                        } else {
                            Searching(N, index + 1);
                        }
                    }
                } else {
                    Searching(N, index + 1);
                }
            }
        }
    }
}

int main(void){
    int N;
    int index = 0;

    cin >> N;
    Searching(N, index);

    cout << counter << "\n";

    return 0;
}