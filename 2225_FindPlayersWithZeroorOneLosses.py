# 2225. Find Players With Zero or One Losses
# You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

# Return a list answer of size 2 where:

# answer[0] is a list of all players that have not lost any matches.
# answer[1] is a list of all players that have lost exactly one match.
# The values in the two lists should be returned in increasing order.

# Note:

# You should only consider the players that have played at least one match.
# The testcases will be generated such that no two matches will have the same outcome.
 
from collections import defaultdict
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = defaultdict(int)
        for w, l in matches:
            losses[l] += 1
        no_losses = sorted({w for w, _ in matches if losses[w] == 0})
        one_loss = sorted({l for l in losses if losses[l] == 1})
        return no_losses, one_loss
