#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
  string t, u;
  cin >> t;
  cin >> u;

  for (int i = 0; i < t.size() - u.size(); i++) {
    for (int j = 0; j < u.size(); j++) {
      if (t[i] != u[j] || t[i] != '?') {
        break;
      }
      if (j == u.size() -1) {
        cout << "Yes" << endl;
        return 0;
      }
    }
  }
  cout << "No" << endl;
  return 0;
}
