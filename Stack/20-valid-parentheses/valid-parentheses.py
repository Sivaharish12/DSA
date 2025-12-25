class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        h = {')': '(', ']': '[', '}': '{'}
        for ch in s:
            if ch in h.values():          
                st.append(ch)
            else:                         
                if not st or st[-1] != h[ch]:
                    return False
                st.pop()

        return not st
