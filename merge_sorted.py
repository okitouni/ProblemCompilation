import heapq

def merge_sorted(arrays):
    heap = []
    merged = []
    for i in range(len(arrays)):
        heap.append((arrays[i].pop(0), i))
    heapq.heapify(heap)
    while heap:
        value, arr_idx = heapq.heappop(heap)
        if arrays[arr_idx]: heapq.heappush(heap, (arrays[arr_idx].pop(0), arr_idx))
        merged.append(value)
    return merged

    
print(merge_sorted([[2,4,6], [1,3,5]]))