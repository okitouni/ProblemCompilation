from collections import OrderedDict

def build_order(reqs):
    visited = OrderedDict()
    def _build(package):
        if package in visited: return
        if package in building:
            raise ValueError(f"found depedency cycle while building {package}")
        building.add(package)
        for dep in reqs[package]:
            _build(dep)
        visited[package] = None
    for package in reqs:
        building = set()
        _build(package)
    return list(visited.keys())





reqs = {0: [],
1: [0],
2: [1],
3: [1, 2],
4: [3, 2]}

print(build_order(reqs))
