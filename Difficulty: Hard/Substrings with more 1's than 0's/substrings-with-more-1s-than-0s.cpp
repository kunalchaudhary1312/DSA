class Solution {
public:
    int countSubstring(string& s) {
        int n = s.length();
        vector<int> bit(2 * n + 2, 0);
        
        auto add = [&](int idx, int val) {
            for (; idx <= 2 * n + 1; idx += idx & -idx) {
                bit[idx] += val;
            }
        };
        
        auto query = [&](int idx) {
            int sum = 0;
            for (; idx > 0; idx -= idx & -idx) {
                sum += bit[idx];
            }
            return sum;
        };
        
        int offset = n + 1;
        add(offset, 1);
        
        int curr_sum = 0;
        int ans = 0;
        
        for (char c : s) {
            curr_sum += (c == '1' ? 1 : -1);
            ans += query(curr_sum + offset - 1);
            add(curr_sum + offset, 1);
        }
        
        return ans;
    }
};