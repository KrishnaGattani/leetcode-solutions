class Solution:
    def findRelativeRanks(self, score):
        sorted_score = sorted(score, reverse=True)
        result = []

        for s in score:
            rank = sorted_score.index(s) + 1

            if rank == 1:
                result.append("Gold Medal")
            elif rank == 2:
                result.append("Silver Medal")
            elif rank == 3:
                result.append("Bronze Medal")
            else:
                result.append(str(rank))

        return result