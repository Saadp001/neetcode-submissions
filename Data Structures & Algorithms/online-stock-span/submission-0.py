class StockSpanner:
    def __init__(self):
        self.stack = []  # stores (price, span) pairs

    def next(self, price: int) -> int:
        span = 1  # at minimum, today counts

        # pop all days with price <= today's price
        # and accumulate their spans
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]  # add popped element's span
            self.stack.pop()

        self.stack.append((price, span))
        return span