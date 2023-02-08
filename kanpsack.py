def knapsack(items, maxWeight):
    cache = {}
    def knapsack_r(item_idx, weight):
        if (item_idx, weight) in cache:
            return cache[(item_idx, weight)]
        if item_idx == -1 or weight <0:
            return 0
        without_item = knapsack_r(item_idx-1, weight)
        item_w, item_val = items[item_idx]
        if weight-item_w >= 0:
            with_item =  knapsack_r(item_idx-1, weight-item_w) + item_val
        else:
            with_item = 0
        best_value = max(with_item, without_item)
        cache[(item_idx, weight)] = best_value
        return best_value

    def knapsack_i():
        DP = [[0]*(maxWeight+1) for _ in range(2)]
        for item in items:
            DP[0][:] = DP[1][:]
            for weight_idx in range(item[0],maxWeight+1):
                DP[1][weight_idx] = max(DP[0][weight_idx],\
                    DP[0][weight_idx-item[0]] + item[1])
        return DP[-1][-1]
    # return knapsack_r(len(items)-1, maxWeight)
    return knapsack_i()

items = [(1,6), (2,10), (3,12), (1,10)]
maxWeight = 5

print(knapsack(items, maxWeight))

