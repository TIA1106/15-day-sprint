
class Solution(object):
    def minWindow(self, s, t):
        if not t or not s:
            return ""

        t_count = {}
        for c in t:
            t_count[c] = t_count.get(c, 0) + 1

        window = {}
        have, need = 0, len(t_count)
        res = ""
        res_len = float("inf")
        left = 0

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            if c in t_count and window[c] == t_count[c]:
                have += 1

            while have == need:
                if (right - left + 1) < res_len:
                    res = s[left:right+1]
                    res_len = right - left + 1
                window[s[left]] -= 1
                if s[left] in t_count and window[s[left]] < t_count[s[left]]:
                    have -= 1
                left += 1

        return res
