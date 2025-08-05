// https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_2_B&lang=ja

#include <iostream>
using namespace std;

int selectionSort(int A[], int N) {
  int sw = 0;
  for (int i = 0; i < N - 1; i++) {
    int minj = i;
    for (int j = i; j < N; j++) {
      if (A[j] < A[minj]) minj = j;
    }
  if (i != minj) {
    swap(A[i], A[minj]);
    sw++;
  };
  }
  return sw;
}

int main() {
  int N, A[100], sw;
  cin >> N;
  for (int i = 0; i < N; i++) {
    cin >> A[i];
  }

  sw = selectionSort(A, N);
  for (int i = 0; i < N; i++) {
    if (i) cout << " ";
    cout << A[i];
  }
  cout << endl;
  cout << sw << endl;

  return 0;
}