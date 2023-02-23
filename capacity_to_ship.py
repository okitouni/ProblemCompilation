# 1011. Capacity To Ship Packages Within D Days
# A conveyor belt has packages that must be shipped from one port to another within days days.

# The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.
from typing import List

def shipWithinDays(weights: List[int], days: int) -> int:
        max_weight = max(weights)
        sum_weight = sum(weights)
        low = max_weight
        high = sum_weight
        
        def can_ship(capacity: int):
            days_needed = 1
            todays_load = 0
            for weight in weights:
                todays_load += weight
                if todays_load > capacity:
                    todays_load = weight
                    days_needed+=1
                    if days_needed > days:
                        return False
            return True

        if can_ship(low): return low
        low += 1
        while low < high:
            mid = (high + low)//2
            if can_ship(mid):
                high = mid
            else:
                low = mid + 1
        return low

weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
print(shipWithinDays(weights, days))