class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #s.reverse()
        #449ms
        """
        for i in range(int(len(s)/2)):
            #print(s[i], s[(len(s) - 1) - i])
            if s[i] != s[(len(s) - 1) - i]:
                tmp = s[i]
                s[i] = s[(len(s) - 1) - i]
                s[(len(s) - 1) - i] = tmp
        """
        #472ms
        
        for i in range(int(len(s)/2)):
            s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]
        #504ms
        
        #print(s)