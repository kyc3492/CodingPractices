#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main(void){
    vector<int> arr = {};
    int m = 0;
    string o = "";
    int n = 0;

    cin >> m;

    for(int i = 0; i < m; i++){
        //cout << i << " index\n";
        cin >> o;
        if(o.find("all") == 0){
            //cout << "all\n";
            arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20};
        }
        else if(o.find("empty") == 0){
            //cout << "empty\n";
            arr.clear();
        }
        else{
            cin >> n;

            if(o.find("add") == 0){
                //cout << "add\n";
                arr.push_back(n);
            }
            else if(o.find("remove") == 0){
                //cout << "remove\n";
                for(int j = 0; j < arr.size(); j++){
                    if (arr[j] == n){
                        arr.erase(arr.begin() + j);
                    } else {
                        continue;
                    }
                }
            }
            else if(o.find("check") == 0){
                //cout << "checking " << n <<"\n";
                bool isExist = false;
                for(int j = 0; j < arr.size(); j++){
                    if (arr[j] == n){
                        isExist = true;
                        break;
                    }
                }

                if(isExist == true){
                    cout << 1 << "\n";
                } else {
                    cout << 0 << "\n";
                }
            }
            else if(o.find("toggle") == 0){
                //cout << "toggle\n";
                bool isExist = false;
                int k = 0;
                for(int j = 0; j < arr.size(); j++){
                    if (arr[j] == n){
                        isExist = true;
                        k = j;
                        break;
                    }
                }

                if(isExist == true){
                    arr.erase(arr.begin() + k);
                } else {
                    arr.push_back(n);
                }
            }
        }

        /*
        cout << "Array!\n";
        for(int j = 0; j < arr.size(); j++){
            cout << arr[j] << " ";
        }
        cout << endl;
        */

        o.clear();
    }
}