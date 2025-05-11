#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main(){
    string s;
    cin >> s;

    string alphabet = "abcdefghijklmnopqrstuvwxyz";
    
    for (int i = 0; i < alphabet.size(); i++){
        if (s.find(alphabet[i]) == string::npos){
            cout << alphabet[i] << endl;
            return 0;
        }
    }

} 
