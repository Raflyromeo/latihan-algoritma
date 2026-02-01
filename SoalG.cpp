#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;

        long long top[200005];
        long long bottom[200005];

        for (int i = 0; i < n; i++) {
            cin >> top[i];
        }
        for (int i = 0; i < n; i++) {
            cin >> bottom[i];
        }

        long long ans = 0;

        for (int i = 0; i < n; i++) {
            long long sum = 0;
            for (int j = 0; j < i; j++) {
                sum += top[j];
            }
            for (int j = i; j < n; j++) {
                sum += bottom[j];
            }
            if (sum > ans) {
                ans = sum;
            }
        }

        cout << ans << '\n';
    }

    return 0;
}
