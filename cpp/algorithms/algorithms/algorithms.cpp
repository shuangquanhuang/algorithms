/*
ID: shuangq1
TASK: holstein
LANG: C++
*/

#include <iostream>
#include <algorithm>


using namespace std;

const int INF = 1000000007;
const double eps = 0.000001;
const int MAXN = 5001;


int N;
int V;

long long E[MAXN], st[MAXN];
long long S;
long long dp[MAXN][MAXN];


int main() {
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(nullptr);

	cin >> N >> S;
	for (int i = 0; i < N; i++) {
		cin >> E[i];
	}

	for (size_t i = 0; i <= N; i++)
	{
		for (size_t j = 0; j <= N; j++) {
			dp[i][j] = 0LL;
		}
	}

	long long s = S;
	st[0] = s;
	for (size_t i = 1; i < N; i++) {
		long long ds = 0, ts = s;
		while (ts > 0) {
			ds += ts % 10;
			ts /= 10;
		}

		s += ds * ds * ds;
		st[i] = s;
	}

	for (size_t i = 1; i <= N; i++) {
		long long se = 0;
		for (size_t si = 0; si < i; si++) {
			se += E[si];
		}
		dp[i][0] = se * S;
		for (size_t j = 1; j <= i; j++) {
			dp[i][j] = max(dp[i-1][j-1], i-1>=j ? (dp[i-1][j] + st[j] * E[i-1]) : 0 );
		}
	}

	long long ans = 0LL;
	for (size_t i = 0; i <= N; i++) {
		ans = max(ans, dp[N][i]);
	}
	cout << ans << endl;


	return 0;
}