from collections import OrderedDict

cache = OrderedDict()

cache[1] = 1
cache[2] = 2
cache[3] = 3

# get last item
print(cache.popitem(last=True))
