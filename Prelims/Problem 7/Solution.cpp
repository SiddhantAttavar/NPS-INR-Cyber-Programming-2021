#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;

int main() {
    // Take input
    int n, k;
    cin >> n >> k;
    int a[n];
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    // Initialize res and pair sum set
    ll res = 0;
    unordered_map<int, int> freq;
    for (int i = 2; i < n - 1; i++) {
        // Add pair sums to the set for j < i - 1
        for (int j = 0; j < i - 1; j++) {
            freq[a[j] + a[i - 1]]++;
        }

        // Add to final answer
        for (int j = i + 1; j < n; j++) {
            if (freq.find(k - (a[i] + a[j])) != freq.end()) {
                res += freq[k - (a[i] + a[j])];
            }
        }
    }

    // Print result
    cout << res << endl;
}
