class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        k=len(words[0])
        m=len(target)
        cnt=[[0]*26 for _ in range(k)]
        for i in range(k):
            for word in words:
                cnt[i][ord(word[i])-ord('a')]+=1
        @lru_cache(None)
        def dfs(i,t):
            if t==m:
                return 1
            if i>=k:
                return 0
            res=0
            if cnt[i][ord(target[t])-ord('a')]>0:
                res+=cnt[i][ord(target[t])-ord('a')]*dfs(i+1,t+1)
            res+=dfs(i+1,t)
            return res
            
                 
        return dfs(0,0)%(10**9+7)
