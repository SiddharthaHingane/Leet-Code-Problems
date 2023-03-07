class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        i, j = 0, len(tokens)
        score = 0
        tsort = sorted(tokens)
        while i < j:
            if power >= tsort[i]:
                power -= tsort[i]
                score += 1
                i += 1
            else:
                if i + 1 < j and score > 0:
                    power += tsort[j - 1]
                    j -= 1
                    score -= 1
                else:
                    break
        return score
