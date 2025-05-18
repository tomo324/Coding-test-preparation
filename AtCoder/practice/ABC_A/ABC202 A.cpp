#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
  int a, b, c;
  cin >> a >> b >> c;
  int ans = 0;
  int ba, bb, bc;
  ba = 7 - a;
  bb = 7 - b;
  bc = 7 - c;
  ans = ba + bb + bc;
  cout << ans << endl;
  return 0;
}