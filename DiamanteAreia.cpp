#include <iostream>
#include <queue>

using namespace std;

int main(){
    int n, i, diamantes;
    string inp;

    cin >> n;
    while(n--){
        cin >> inp;

        queue<char> Q;

        diamantes = 0;
        for(i = 0; i < inp.length(); i++){
            switch(inp[i]){
                case '<':
                    Q.push('<');
                    break;

                case '>':
                    if(!Q.empty()){
                        Q.pop();
                        diamantes++;
                    }
                    break;

                default:
                    break;
            }
        }

        cout << diamantes << endl;
    }

    return 0;
}