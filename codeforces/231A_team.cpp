// i = int(input())

// count = 0

// for _ in range(i):
//     s = list(map(int, input().split()))
//     if sum(s)>=2:
//         count += 1

// print(count)

#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int count = 0;
    for (int i = 0; i < n; i++)
    {
        int a, b, c;
        cin >> a >> b >> c;
        if (a + b + c >= 2)
        {
            count++;
        }
    }
    cout << count << endl;
    return 0;
}