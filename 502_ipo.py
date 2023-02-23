# Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.

# You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it.

# Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

# Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.

# The answer is guaranteed to fit in a 32-bit signed integer.
from typing import List
import heapq
import math

def find_max_capital(k: int, w: int, profits: List[int], capital: List[int]) -> int:
    if w > max(capital):
        return w + sum(heapq.nlargest(k, profits))
    def use_priority_q(w=w):
        priority_q = []
        q = [(c,p) for p,c in zip(profits, capital)]
        heapq.heapify(q)
        for _ in range(k):
            while q and q[0][0] <= w:
                _, p = heapq.heappop(q)
                heapq.heappush(priority_q, (-p))
            if priority_q:
                w -=  heapq.heappop(priority_q)
            else: break
        return w
    
    def use_linear_search(w=w):
        max_profit = 0
        for _ in range(k):
            for p,c in zip(profits, capital):
                if c <= w:
                    max_profit = max(max_profit, p)
            w += max_profit
        return w
    
    if k < math.log2(len(profits)):
        return use_linear_search()
    return use_priority_q()

k = 2
w = 0
profits = [1, 2, 3]
capital = [0, 1, 1]
print(find_max_capital(k, w, profits, capital))
        

