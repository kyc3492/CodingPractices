#include <iostream>
#include <cmath>
#define MAX 1000
using namespace std;

int main(){
	int x, y, w, h, dis;
	cin >> x >> y >> w >> h;
	
	dis = x;
	if(dis > y){
		dis = y;
	}
	if(dis > w - x){
		dis = w - x;
	}
	if(dis > h - y){
		dis = h - y;
	}
	
	cout << dis << endl;
	return 0;
}