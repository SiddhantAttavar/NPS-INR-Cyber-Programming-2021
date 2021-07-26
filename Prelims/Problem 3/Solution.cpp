#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;

int main() {
    // Take input
    int n;
    cin >> n;
    ll a[n], b[n];
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    for (int i = 0; i < n; i++) {
        cin >> b[i];
    }

    // Find the values of array c
    ll c[n];
    for (int i = 0; i < n; i++) {
        c[i] = a[i] * b[i];
    }

    // Print the result
    for (int i = 0; i < n; i++) {
        cout << c[i] << ' ';
    }
}