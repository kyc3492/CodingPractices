using namespace std;
#include <string>
#include <iostream>

class Solution {
public:
    int addDigits(int num) {
        int answer = -1;
        string s_num = to_string(num);
        
        while (answer > 9 or answer == -1){
            int tmp = 0;
            for (int i = s_num.size() - 1; i >= 0; i--){
                tmp += s_num[i] - '0';
            }
            cout << tmp << "\n";
            s_num = to_string(tmp);
            answer = tmp;
        }
        
        return answer;
    }
};