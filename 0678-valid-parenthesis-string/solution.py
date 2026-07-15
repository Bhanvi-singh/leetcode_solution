class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        os = []
        ss = []
        n = len(s)
        for i in range(n):
            if  s[i] == '(':
                os.append(i)
            elif  s[i] == '*':
                ss.append(i)
            else:
                if os:
                    os.pop()
                elif ss:
                    ss.pop()
                else:
                    return False
        while os and ss:
            if os[-1]  < ss[-1]:
                os.pop()
                ss.pop()
            else:
                return False
        return len(os) == 0
