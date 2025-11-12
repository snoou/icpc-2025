#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int n;
ll k;
vector<vector<int>> g;
vector<int> sz;
vector<bool> blocked;
int needT;

void dfs_size(int u, int p) {
    sz[u] = 1;
    for (int v : g[u])
        if (v != p && !blocked[v]) {
            dfs_size(v, u);
            sz[u] += sz[v];
        }
}

int dfs_centroid(int u, int p, int total) {
    for (int v : g[u])
        if (v != p && !blocked[v] && sz[v] > total / 2)
            return dfs_centroid(v, u, total);
    return u;
}

void collect_distances(int u, int p, int depth, vector<int>& out) {
    out.push_back(depth);
    for (int v : g[u])
        if (v != p && !blocked[v])
            collect_distances(v, u, depth + 1, out);
}

// count pairs (a,b) with a in A, b in B, and a + b < needT
ll count_pairs_sum_less(const vector<int>& A, const vector<int>& B) {
    ll cnt = 0;
    int j = (int)B.size() - 1;
    for (int i = 0; i < (int)A.size(); ++i) {
        while (j >= 0 && A[i] + B[j] >= needT) --j;
        if (j < 0) break;
        cnt += (j + 1);
    }
    return cnt;
}

vector<int> merge_sorted(const vector<int>& A, const vector<int>& B) {
    vector<int> merged;
    merged.reserve(A.size() + B.size());
    int i = 0, j = 0;
    while (i < (int)A.size() && j < (int)B.size()) {
        if (A[i] <= B[j]) merged.push_back(A[i++]);
        else merged.push_back(B[j++]);
    }
    while (i < (int)A.size()) merged.push_back(A[i++]);
    while (j < (int)B.size()) merged.push_back(B[j++]);
    return merged;
}

ll solve_centroid(int start) {
    dfs_size(start, -1);
    int c = dfs_centroid(start, -1, sz[start]);
    blocked[c] = true;

    ll local_count = 0;
    vector<int> all = {0};

    for (int v : g[c]) if (!blocked[v]) {
        vector<int> sub;
        collect_distances(v, c, 1, sub);
        sort(sub.begin(), sub.end());
        sort(all.begin(), all.end());
        local_count += count_pairs_sum_less(sub, all);
        all = merge_sorted(all, sub);
    }

    for (int v : g[c]) if (!blocked[v])
        local_count += solve_centroid(v);

    return local_count;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> k;
    g.assign(n, {});
    for (int i = 0; i < n - 1; ++i) {
        int u, v; cin >> u >> v;
        --u; --v;
        g[u].push_back(v);
        g[v].push_back(u);
    }

    int t = (n - 1) - (int)k;
    if (t <= 0) {
        cout << (ll)n * (n - 1) / 2 << '\n';
        return 0;
    }

    needT = t;
    sz.assign(n, 0);
    blocked.assign(n, false);
    ll pairs_lt_t = solve_centroid(0);
    ll total = (ll)n * (n - 1) / 2;
    ll ans = total - pairs_lt_t;
    cout << ans << '\n';
    return 0;
}
