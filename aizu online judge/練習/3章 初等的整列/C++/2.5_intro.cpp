// https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_D&lang=jp

#include <iostream>
#include <algorithm>

using namespace std;
static const int MAX = 200000;

int main() {
  int n, r;

  cin >> n;
  cin >> r;

  int maxv = -2e9;
  int minv = r;

  for (int i = 1; i < n; i++) {
    cin >> r;
    maxv = max(maxv, r - minv);
    minv = min(minv, r);
  };

  cout << maxv << endl;

  return 0;
}