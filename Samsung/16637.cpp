#include <iostream>
#include <string.h>
using namespace std;

int N;
int NUMBERS[20];
char *OPERATIONS[20];

int main(void){
    int tmp;

    cin >> N;
    
    for(int i = 0; i < N; i++){
        if(i % 2 == 0){
            cin >> NUMBERS[i];
            cout << NUMBERS[i];
        } else {
            cin.getline(OPERATIONS[i]);
            cout << OPERATIONS[i];
        }
    }

    for(int i = 0; i < N; i++){
        if(i % 2 == 1){
            if(strcmp(OPERATIONS[i], "+") == 0){
                cout << NUMBERS[i - 1] << OPERATIONS[i] << NUMBERS[i + 1] << "\n";
                NUMBERS[i + 1] = NUMBERS[i - 1] + NUMBERS[i + 1];
            } else if(strcmp(OPERATIONS[i], "-") == 0){
                cout << NUMBERS[i - 1] << OPERATIONS[i] << NUMBERS[i + 1] << "\n";
                NUMBERS[i + 1] = NUMBERS[i - 1] - NUMBERS[i + 1];
            } else if(strcmp(OPERATIONS[i], "*") == 0){
                cout << NUMBERS[i - 1] << OPERATIONS[i] << NUMBERS[i + 1] << "\n";
                NUMBERS[i + 1] = NUMBERS[i - 1] * NUMBERS[i + 1];
            }

            if(strcmp(OPERATIONS[i], NULL) == 0){
                cout << NUMBERS[i + 1];
            }
        }
    }
}