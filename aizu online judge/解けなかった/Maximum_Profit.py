"""
https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_D&lang=ja

forでi + 1以降の最も大きい値を基準にして引き算をする
その答えが現時点の最大値より大きければ最大値を更新する
"""
"""
n = int(input())
nums_list = []
max_value = -10 ** 9
# 受け取った値をリストにまとめる
for i in range(n):
    num = int(input())
    nums_list.append(num)

for i in range(n - 1):
    m_num = max(nums_list[i + 1:])
    result = (m_num - nums_list[i])
    if result > max_value:
        max_value = result

print(max_value)
--------------------------------------------------
# 正解のコード
n = int(input())
R = [int(input()) for i in range(n)]

maxv = -2000000000
minv = R[0]

for i in range(1, n):
    maxv = max(maxv, R[i] - minv)
    minv = min(minv, R[i])

print(maxv)


"""
# ------------------------------------------------------------------------
# 再現

n = int(input())
R = [int(input()) for i in range(n)]

maxv = -10 ** 9
minv = R[0]

for i in range(1, n):
    maxv = max(maxv, R[i] - minv)
    minv = min(minv, R[i])

print(maxv)


"""
--------------------------------------------------------------------------------
C++のコード


#include<iostream>
#include<algorithm>
using namespace std;
static const int MAX = 200000;

int main() {
    int R[MAX], n;

    cin >> n;
    for ( int i = 0; i < n; i++) cin >> R[i];

    int maxv = -2000000000;
    int minv = R[0]

    for ( int i = 1; i < n; i++) {
        maxv = max(maxv, R[i] - minv);
        minv = min(minv, R[i]):
    }

    cout << maxv << endl;

    return 0;
}
"""