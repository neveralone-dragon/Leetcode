class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l = []
        for i in s:
            if i.isalpha():
                l.append(i)
            elif i.isdigit():
                l.append(i)
        res = ''.join(l)
        return res == res[::-1]
