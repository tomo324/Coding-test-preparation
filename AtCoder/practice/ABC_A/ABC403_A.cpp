#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main(){
  int N;
  cin >> N;

  vector<int> A(N);
  for (int i = 0; i < N; i++) {
    cin >> A[i];
  }

  int ans = 0;
  for (int i = 0; i < N; i++) {
    if (i % 2 == 0) {
      ans += A[i];
    }
  }
  cout << ans << endl;
  return 0;
  }