class StockSpanner:

    def __init__(self):
        self.span_tracker = []

    def next(self, price: int) -> int:
        span = 1
        while self.span_tracker and self.span_tracker[-1][0] <= price:
            span += self.span_tracker[-1][1]
            self.span_tracker.pop()
        self.span_tracker.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)