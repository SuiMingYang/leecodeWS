import functools

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if not len(s1) + len(s2) == len(s3): return False
    
        @functools.lru_cache(None)
        def restore(s1, s2, s3):
            if s3 == '':
                return True
            
            r1, r2 = False, False
            if s1 and s3[0] == s1[0]:
                r1 = restore(s1[1:], s2, s3[1:])
            
            if s2 and s3[0] == s2[0]:
                r2 = restore(s1, s2[1:], s3[1:])
                
            return r1 or r2
        
        return restore(s1, s2, s3)


obj=Solution()
print(obj.isInterleave(s1 = "aabcca", s2 = "dbbca", s3 = "aadbbbccca"))