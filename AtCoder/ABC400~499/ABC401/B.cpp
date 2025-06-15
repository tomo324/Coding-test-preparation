#include <bits/stdc++.h>

using namespace std;

int main() {
  int N;
  cin >> N;
  
  bool isValid = false;
  int cntError = 0;

  for (int i = 0; i < N; i++) {
    string S;
    cin >> S;

    if (S == "login") {
      isValid = true;
    }

    if (S == "logout") {
      isValid = false;
    }

    if (!isValid && S == "private") {
      cntError++;
    }
  }

  cout << cntError << endl;
  return 0;

}