class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        totalword = {}
        for b in words2:
            tmp = Counter(b)
            for k,v in tmp.items():
                if k not in totalword:
                    totalword[k] = v
                else:
                    totalword[k] = max(v,totalword[k])
        output = []
        for a in words1:
            tmp = Counter(a)
            if all([k in tmp and v <= tmp[k] for k,v in totalword.items()]):
                output.append(a)
        return output
