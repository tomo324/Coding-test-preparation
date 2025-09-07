#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
  int N;
  cin >> N;
  vector<string> S(N);
  int X;
  string Y;

  for (int i = 0; i < N; i++) {
    cin >> S[i];
  }
  cin >> X >> Y;

  if (S[X-1] == Y) {
    cout << "Yes" << endl;
  } else {
    cout << "No" << endl;
  }
  return 0;
}