steps = [1, 2, 3]
total_steps = 3

def get_n_ways(steps, total_steps, recursive=True):
    n_ways = [0] * (total_steps + 1)
    n_ways[0] = 1
    if not recursive:
        for i in range(0, total_steps + 1):
            for step in steps:
                if i + step > total_steps: continue
                n_ways[i + step] += n_ways[i]
            print(n_ways)
        
    else:
        def _n_ways(total, steps_):
            if total < 0:
                return 0
            if n_ways[total]: return n_ways[total]
            n_ways_to_total = 0
            for i, step in enumerate(steps_):
                n_ways_to_total += _n_ways(total - step, steps_[:i+1])
            n_ways[total] = n_ways_to_total # wrong caching
            print(n_ways)
            return n_ways_to_total
        _n_ways(total=total_steps, steps_=steps)
    return n_ways[-1]

# print(get_n_ways(steps, 5))

def deco(func):
    memory = {}
    def wrapped(*args):
        if args not in memory:
            memory[args] = func(args)
            print("unknown")
        print(memory)
        return memory[args]
    return wrapped

@deco
def test(a):
    print(a)
    return a

test("a")
test("b")
test("a")