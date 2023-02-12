# codebases with different dependencies and build times.
# goal is to find the optimal build order for a given set of codebases
# result is a list of codebases in the order they should be built
# result = [ [time_to_build, *codebases] for each step ]
import heapq

def optimal_build(codebases, deps):
    built = set()
    building = set()
    leaf_nodes = []
    for codebase, time in codebases:
        if codebase not in deps:
            heapq.heappush(leaf_nodes, (time, codebase))
            building.add(codebase)

    result = []
    t = 0
    while leaf_nodes:
        print(f"t: {t}s | building", *leaf_nodes)
        time, codebase = heapq.heappop(leaf_nodes)
        t += time

        built.add(codebase)
        leaf_nodes = [(t-time, cb) for t, cb in leaf_nodes]

        result.append([time, codebase, *(cb for t, cb in leaf_nodes)])

        # also pop things that finished at the same time
        while leaf_nodes and leaf_nodes[0][0] == 0:
            _, cb = heapq.heappop(leaf_nodes)
            built.add(cb)
        # check if anything new can be built
        for codebase, time in codebases: # TODO stop checking every codebase adds an O(N) factor
            if codebase in deps and codebase not in building:
                for dep in deps[codebase]:
                    if dep not in built: break
                else: 
                    heapq.heappush(leaf_nodes, (time, codebase))
                    building.add(codebase)
    print(f"Done! Time elapsed {t}s")
    return result

codebases = [("A", 1), ("B", 1), ("C", 2), ("D", 2), ("E", 3), ("F", 1)]
deps = {"A": ["B", "C"], "C":["D"]}
print(*optimal_build(codebases, deps), sep='\n')


    
