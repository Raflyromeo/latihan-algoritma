#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;

    while (T--) {
        int n;
        cin >> n;

        int a[2][200005];

        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < n; j++) {
                cin >> a[i][j];
            }
        }

        int sum = 0;

        for (int j = 0; j < n; j++) {
            if (a[0][j] > a[1][j]) {
                sum += a[0][j];
            } else {
                sum += a[1][j];
            }
        }

        cout << sum << '\n';
    }

    return 0;
}
