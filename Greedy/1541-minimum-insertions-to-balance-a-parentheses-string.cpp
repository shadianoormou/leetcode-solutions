class Solution {
public:
    int minInsertions(string s) {
        int insertions = 0;
        int needed = 0;

        for (char c : s) {
            if (c == '(') {
                needed += 2;

                if (needed % 2 == 1) {
                    insertions++;
                    needed--;
                }
            } else {
                needed--;

                if (needed == -1) {
                    insertions++;
                    needed = 1;
                }
            }
        }

        return insertions + needed;
    }
};
