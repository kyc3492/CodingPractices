#include <iostream>
#include <string>
#include <cstring>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int m = 0;
    bool S[21] = {false};

    cin >> m;

    for (int i = 0; i < m; i++){
        string op;
        int x;

        cin >> op;

        if (op == "add"){
            cin >> x;
            S[x] = true;
        }
        else if (op == "remove"){
            cin >> x;
            S[x] = false;
        }
        else if (op == "check"){
            cin >> x;
            cout << S[x] << "\n";
        }
        else if (op == "toggle"){
            cin >> x;
            if (S[x] == true){
                S[x] = false;
            } else {
                S[x] = true;
            }
        }
        else if (op == "all"){
            memset(S, true, 21);
        }
        else if (op == "empty"){
            memset(S, false, 21);
        }
    }
    return 0;
}