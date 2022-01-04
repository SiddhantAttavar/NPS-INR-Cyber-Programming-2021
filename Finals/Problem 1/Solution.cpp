#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;

int main() {
    // Take input
    int n;
    cin >> n;
    
    // Create an array dp where dp[i] is answer for N = i + 1
    int dp[n] = {1, 2};
    for (int i = 2; i < n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }

    // The answer is dp[n - 1]
    cout << dp[n - 1] << endl;
}
