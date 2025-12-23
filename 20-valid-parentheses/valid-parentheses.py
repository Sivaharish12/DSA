class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        h={')':'(', ']':'[','}':'{'}
        for i in s:
            if i in ['{','[','(']:
                st.append(i)
            else:
                if len(st)==0: return False
                if h[i]==st[-1]: st.pop()
                else: return False
        if len(st)==0: return True
        else: return False

        