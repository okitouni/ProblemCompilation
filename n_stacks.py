class Stacks:
    def __init__(self, n, capacity):
        self.n = n
        self.stack_data = [0] * capacity
        self.stack_top = [-1] * n
        self.next_available = 0
        self.next_idx = [i+1 for i in range(capacity)]
        self.next_idx[-1] = -1

    def push(self, stack, value):
        current_idx = self.next_available
        self.stack_data[current_idx] = value
        self.next_available = self.next_idx[current_idx]
        self.next_idx[current_idx] = self.stack_top[stack]
        self.stack_top[stack] =current_idx

    def pop(self, stack):
        current_idx = self.stack_top[stack]
        value = self.stack_data[current_idx]
        self.stack_top[stack] = self.next_idx[current_idx]
        self.next_idx[current_idx] = self.next_available
        self.next_available = current_idx
        return value



# data a x x
# nxt  1 -1 -1
#        ^
# nxt_av = 1

#
