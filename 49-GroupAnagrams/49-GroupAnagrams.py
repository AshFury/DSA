# Last updated: 25/05/2025, 21:12:26
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for i in strs:
            c=[0]*26
            for k in i:
                c[ord(k)-ord("a")]+=1
            res[tuple(c)].append(i)
        return res.values()



                
            
        
        