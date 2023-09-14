"""
332. Reconstruct Itinerary
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.


"""
from typing import List
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        destinations = defaultdict(list)

        for start, end in tickets:
            destinations[start].append(end)

        for start, ends in destinations.items():
            ends.sort(reverse=True)
        
        itinerary = []
        visited_stack = ["JFK"]
        # dfs iteratively
        while visited_stack:
            current = visited_stack[-1]
            if destinations[current]:
                next_ = destinations[current].pop()
                visited_stack.append(next_)
            else:
                itinerary.append(visited_stack.pop())
        itinerary.reverse()
        return itinerary
        
        