class Solution {
    set<string> parse(const string& s, int& i) {
        set<string> res;
        set<string> cur = {""};

        while (i < s.size() && s[i] != '}') {
            if (s[i] == ',') {
                res.insert(cur.begin(), cur.end());
                cur = {""};
                i++;
            } else {
                set<string> part;

                if (s[i] == '{') {
                    i++;
                    part = parse(s, i);
                    i++;
                } else {
                    part = {string(1, s[i])};
                    i++;
                }

                set<string> next;

                for (const string& a : cur) {
                    for (const string& b : part) {
                        next.insert(a + b);
                    }
                }

                cur = move(next);
            }
        }

        res.insert(cur.begin(), cur.end());
        return res;
    }

public:
    vector<string> braceExpansionII(string expression) {
        int i = 0;
        set<string> result = parse(expression, i);

        return vector<string>(result.begin(), result.end());
    }
};
