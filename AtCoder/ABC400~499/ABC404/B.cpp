#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int count_diff(vector<string> S, vector<string> T) {
  int N = S.size();
  int ans = 0;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      if (S[i][j] != T[i][j]) ans++;
    }
  }
  return ans;
}

vector<string> rotate(vector<string> S) {
  int N = S.size();
  vector<string> ret(N, string(N, '.'));
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      ret[i][j] = S[N-1-j][i];
    }
  }
  return ret;
}

int main() {
  int N;
  cin >> N;
  vector<string> S(N), T(N);
  for (int i = 0; i < N; i++) cin >> S[i];
  for (int i = 0; i < N; i++) cin >> T[i];

  int ans = 1e9;
  for (int rot_count = 0; rot_count < 4; rot_count++) {
    ans = min(ans, count_diff(S, T) + rot_count);
    S = rotate(S);
  }
  cout << ans << endl;
}