class Solution {
    struct Node {
        int prod;
        long long cnt[5];

        Node() {
            prod = 1;
            for (int i = 0; i < 5; i++) cnt[i] = 0;
        }
    };

    int n, k;
    vector<Node> tree;

    Node mergeNode(const Node& a, const Node& b) {
        Node res;

        res.prod = (long long)a.prod * b.prod % k;

        for (int i = 0; i < k; i++) {
            res.cnt[i] = a.cnt[i];
        }

        for (int r = 0; r < k; r++) {
            int nr = (long long)a.prod * r % k;
            res.cnt[nr] += b.cnt[r];
        }

        return res;
    }

    Node makeNode(int val) {
        Node node;
        node.prod = val % k;
        node.cnt[node.prod] = 1;
        return node;
    }

    void build(int idx, int l, int r, vector<int>& nums) {
        if (l == r) {
            tree[idx] = makeNode(nums[l]);
            return;
        }

        int mid = (l + r) >> 1;

        build(idx << 1, l, mid, nums);
        build(idx << 1 | 1, mid + 1, r, nums);

        tree[idx] = mergeNode(tree[idx << 1], tree[idx << 1 | 1]);
    }

    void update(int idx, int l, int r, int pos, int val) {
        if (l == r) {
            tree[idx] = makeNode(val);
            return;
        }

        int mid = (l + r) >> 1;

        if (pos <= mid)
            update(idx << 1, l, mid, pos, val);
        else
            update(idx << 1 | 1, mid + 1, r, pos, val);

        tree[idx] = mergeNode(tree[idx << 1], tree[idx << 1 | 1]);
    }

    Node query(int idx, int l, int r, int ql) {
        if (ql <= l)
            return tree[idx];

        int mid = (l + r) >> 1;

        if (ql > mid)
            return query(idx << 1 | 1, mid + 1, r, ql);

        Node left = query(idx << 1, l, mid, ql);
        Node right = tree[idx << 1 | 1];

        return mergeNode(left, right);
    }

public:
    vector<int> resultArray(vector<int>& nums, int K,
                            vector<vector<int>>& queries) {
        n = nums.size();
        k = K;

        tree.resize(4 * n);
        build(1, 0, n - 1, nums);

        vector<int> ans;
        ans.reserve(queries.size());

        for (auto& q : queries) {
            update(1, 0, n - 1, q[0], q[1]);

            Node res = query(1, 0, n - 1, q[2]);

            ans.push_back((int)res.cnt[q[3]]);
        }

        return ans;
    }
};
