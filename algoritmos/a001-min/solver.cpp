#include <bits/stdc++.h>

using namespace std;
 

int solve(int n, vector<int> a) {
    if (a.size() == 0) {
        throw invalid_argument("empty list of numbers");
    }

    int min = a[0];
    for (int i=1; i<n; i++) {
        if (a[i] < min) {
            min = a[i];
        }
    }

    return min;
}


int solve_another_implementation(int n, vector<int> a) {
    if (a.size() == 0) {
        throw invalid_argument("empty list of numbers");
    }

    int min = a[--n];
    while (n--) {
        if (a[n] < min) {
            min = a[n];
        }
    }
    return min;
}
 

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;

        vector<int> a(n);
        for (int& x : a) cin >> x;

        int max = solve(n, a);

        cout << max << "\n";
    }
}
