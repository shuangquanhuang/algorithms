#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <functional>
#include <string>
#include <stdio.h>
#include <string.h>


using namespace std;

const int INF = 1000000007;
const double eps = 0.000001;
const int MAXN = 400005;

int parent[MAXN];
int prank[MAXN];

int find(int u) {
	if (parent[u] == u) {
		return u;
	}
	int pu = find(parent[u]);
	parent[u] = pu;

	return pu;
}

bool merge(int u, int v) {
	int pu = find(u);
	int pv = find(v);

	if (pu == pv) {
		return false;
	}

	if (prank[pu] >= prank[pv]) {
		parent[pv] = pu;
		prank[pu] += prank[pv];
	}
	else {
		parent[pu] = pv;
		prank[pv] += prank[pu];
	}

	return true;
}

struct node {
	int to, next;
}E[MAXN];
int head[MAXN];

int cnt = 1;

void add(int from, int to) {
	E[++cnt].next = head[from];
	E[cnt].to = to;
	head[from] = cnt;
}


int main() {
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(0);
	int n, m;
	cin >> n >> m;

	for (int i = 0; i < MAXN; i++) {
		parent[i] = i;
		prank[i] = 1;
	}

	for (int i = 0; i < m; i++) {
		int u, v;
		cin >> u >> v;
		add(u, v);
		add(v, u);
	}


	vector<int> destroy;
	set<int> rest;
	for (int i = 0; i < n; i++)
	{
		rest.insert(i);
	}
	int k;
	cin >> k;
	for (int i = 0; i < k; i++) {
		int u;
		cin >> u;
		destroy.push_back(u);
		rest.erase(u);
	}

	int c = n - destroy.size();
	for (int u: rest)
	{
		for (int vi = head[u]; vi > 0; vi = E[vi].next) {
			int v = E[vi].to;
			if (rest.find(v) != rest.end())
			{
				c -= merge(u, v) ? 1 : 0;
			}
		}
	}

	vector<int> ans;
	ans.push_back(c);

	for (auto it=destroy.rbegin(); it != destroy.rend(); it++)
	{
		c += 1;
		int u = *it;
		for (int vi=head[u]; vi > 0; vi = E[vi].next)
		{	
			int v = E[vi].to;
			if (rest.find(v) != rest.end()) {
				c -= merge(u, v) ? 1 : 0;
			}
		}
		ans.push_back(c);
		rest.insert(u);
	}


	for (auto it = ans.rbegin(); it != ans.rend(); it++) {
		cout << *it << endl;
	}



	return 0;
}
