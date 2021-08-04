#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;

int main() {
    // Take input
    int n;
    cin >> n;
    int a[n];
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    // Create an array best which is the largest sum of a 
    // contiguous subarray that ends at the current index
    ll best[n];
    best[0] = a[0];
    for (int i = 1; i < n; i++) {
        best[i] = max(best[i - 1] + a[i], (ll) a[i]);
    }

    // The answer is the maximum number in best
    cout << *max_element(best, best + n) << endl;
}