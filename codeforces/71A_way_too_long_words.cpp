// n = int(input())
// for _ in range(n):
//     s = input()
//     if len(s) >10:
//         print(f"{s[0]}{len(s)-2}{s[-1]}")
//     else:
//         print(s)

#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        if (s.length() > 10) {
            cout << s[0] << s.length() - 2 << s[s.length() - 1] << endl;
        } else {
            cout << s << endl;
        }
    }
}