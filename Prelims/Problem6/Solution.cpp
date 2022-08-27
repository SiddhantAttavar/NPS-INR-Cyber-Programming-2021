#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;

int main() {
    // Take input
    int n;
    cin >> n;

    // Do a binary search to find the result
    int low = 0, high = n, res = 0;
    while (low <= high) {
        ll mid = (low + high) / 2;
        if (mid * (mid + 1) / 2 <= n) {
            res = mid;
            low = mid + 1;
        }
        else {
            high = mid - 1;
        }
    }

    // Print the result
    cout << res << endl;
}
