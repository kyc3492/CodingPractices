import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        condition = re.compile('[a-z0-9]')
        transformed = ''
        
        for c in s:
            if condition.match(c):
                transformed += c
        
        length = len(transformed)
        
        print(transformed)
        
        for i in range(int(length / 2)):
            print(i, (length - 1) - i)
            if transformed[i] != transformed[(length - 1) - i]:
                print(transformed[i], i,"Not Same",transformed[(length - 1) - i], (length - 1) - i)
                return False
        
        return True

#101ms