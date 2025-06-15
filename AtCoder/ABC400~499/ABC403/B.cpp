#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
  string t, u;
  cin >> t >> u;

  for (int i = 0; i <= t.size() - u.size(); i++) {
    bool match = true;
    for (int j = 0; j < u.size(); j++) {
      // t[i + j] が '?'でない場合で、u[j]と一致しない場合
      if (t[i + j] != '?' && t[i + j] != u[j]) {
        match = false;
        break;
      }
    }
    if (match) {
      cout << "Yes" << endl;
      return 0;
    }
  }
  cout << "No" << endl;
  return 0;
}
