class FreqStack:

    def __init__(self):
        self.stack = []
        self.mp= defaultdict(int) 

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.mp[val] += 1
      

    def pop(self) -> int:
        maxi = max(self.mp.values())
        i = len(self.stack) - 1

        while self.mp[self.stack[i]] != maxi:
            i -=1

        self.mp[self.stack[i]] -= 1
        return self.stack.pop(i)   


      
        




