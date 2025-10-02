#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
  int q;
  cin >> q;
  queue<int> que;
  for (int i = 0; i < q; i++) {
    int t, x;
    cin >> t;
    if (t == 1) {
      cin >> x;
      que.push(x);
    } else {
      cout << que.front() << endl;
      que.pop();
    }
  }
}