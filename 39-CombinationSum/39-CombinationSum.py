# Last updated: 09/09/2025, 09:56:42
class Solution:
    def makecombo(self, arr, curr, res, remsum, index):
        if remsum==0:
            res.append(list(curr))
            return
        elif remsum<0 or index>=len(arr):
            return
        curr.append(arr[index])
        self.makecombo(arr,curr,res,remsum-arr[index],index)
        curr.pop()
        self.makecombo(arr,curr,res,remsum,index+1)        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        curr=[]
        res=[]
        candidates.sort()
        self.makecombo(candidates,curr,res,target,0)
        return res