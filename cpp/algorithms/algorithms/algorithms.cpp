/*
ID: shuangq1
TASK: holstein
LANG: C++
*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <set>
#include <queue>
#include <ostream>
#include <istream>
#include <typeinfo>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <limits>
#include <fstream>
#include <array>
#include <list>
#include <bitset>
#include <functional>
#include <random>
#include <string>
#include <tuple>
#include <string.h>
#include <chrono>

using namespace std;
using namespace std::chrono;


#define pb push_back
#define pp pop_back
#define pf push_front
#define ppf pop_front
#define _ inline
#define fst first
#define sec second
#define ins insert
#define ers erase
#define mp make_pair
#define mt make_tuple
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define sz size
#define rsz resize
#define pw2(x) (1<<(x))
#define chcpy(Vec) copy(Vec.begin(), Vec.end(), ostream_iterator<char>(cout))
#define intcpy(Vec) copy(Vec.begin(), Vec.end(), ostream_iterator<int>(cout, " "))
#define elif else if
#define uset unordered_set
#define umap uorderd_map
#define rep(i, l, r) for(int i=l; i<r; i++)
#define rep2(i, l, r) for(int i=l; i<=r; i++)
#define rrep(i, l, r) for(int i=l; i>r; i--)
#define rrep2(i, l, r) for(int i=l; i>=r; i--)


typedef long L;
typedef long long LL;
typedef pair<int, int> PII;
typedef pair<long, long> PLL;
typedef double LD;
typedef unsigned int UINT;
typedef unsigned long long ULL;
typedef unsigned long UL;
typedef vector<vector<int>> VVI;
typedef vector<vector<UINT>> VVUINT;
typedef vector<vector<L>> VVL;
typedef vector<vector<LL>> VVLL;
typedef vector<int> VI;
typedef vector<long> VL;
typedef vector<LL> VLL;
typedef vector<PII> VPII;
typedef vector<PLL> VPLL;
typedef vector<LD> VLD;
typedef vector<bool> VB;
typedef tuple<LL, LL, LL> TLLL;
typedef tuple<int, int, int> TIII;

const int INF = 1000000007;
const double eps = 0.000001;
const int MAXN = 1001;

int bisect_right(int* arr, int n, int val) {
	int l = 0;
	int r = n + 1;
	while (l < r) {
		int m = (l + r) / 2;
		if (arr[m] <= val) {
			l = m + 1;
		}
		else {
			r = m;
		}
	}

	return l;
}


int N;
int V;
int A[MAXN][26];
bool used[MAXN];
int vol[26];
int cost = 1 << 30;
vector<int> ans;

void dfs(int index) {
	int valid = true;
	int c = 0;
	vector<int> s;
	for (size_t i = 0; i < V; i++)
	{
		if (vol[i] < A[0][i]) {
			valid = false;
			break;
		}
		c += vol[i];
	}

	if (valid )
	{
		for (int i = 1; i <= N; i++)
		{
			if (used[i]) {
				s.push_back(i);
			}
		}

		if (c < cost || (c==cost && s.size() < ans.size()))
		{
			cost = c;
			ans.clear();
			copy(s.begin(), s.end(), back_inserter(ans));
		}
	}

	if (index > N) {
		return;
	}

	dfs(index + 1);
	used[index] = true;
	for (size_t i = 0; i < V; i++)
	{
		vol[i] += A[index][i];
	}
	dfs(index + 1);
	used[index] = false;
	for (size_t i = 0; i < V; i++)
	{
		vol[i] -= A[index][i];
	}
}

int main() {
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(nullptr);

#ifdef OFFLINE
	ifstream fin("input.txt");
	cin.rdbuf(fin.rdbuf()); // assign file's streambuf to cin
	high_resolution_clock::time_point t1 = high_resolution_clock::now();
#endif


	ifstream fin("holstein.in");
	ofstream fout("holstein.out");
	fin >> V;
	for (int i = 0; i < V; i++) {
		fin >> A[0][i];
	}

	fin >> N;
	for (int i = 1; i <= N; i++) {
		for (size_t j = 0; j < V; j++)
		{
			fin >> A[i][j];
		}
	}

	dfs(1);

	fout << ans.size();
	for (int v : ans) {
		cout << " " << v;
	}
	fout << endl;



	
#ifdef OFFLINE
	high_resolution_clock::time_point t2 = high_resolution_clock::now();
#endif

#ifdef OFFLINE
	high_resolution_clock::time_point t3 = high_resolution_clock::now();
	auto duration = duration_cast<seconds>(t3 - t1).count();
	auto outcost = duration_cast<seconds>(t3 - t2).count();
	cout << "time cost: " << duration << "s, output cost: " << outcost << "s" << endl;
#endif

	return 0;
}