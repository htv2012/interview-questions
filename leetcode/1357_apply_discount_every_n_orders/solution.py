

class Cashier:
    def __init__(self, n: int, discount: int, products: list[int], prices: list[int]):
        self.n = n
        self.discount = discount
        self.prices = dict(zip(products, prices))
        self.count = 0

    def getBill(self, product: list[int], amount: list[int]) -> float:
        self.count += 1
        total = sum(self.prices[i] * amt for i, amt in zip(product, amount))
        if self.count % self.n == 0:
            total = total * ((100 - self.discount) / 100)
        # total = int(total)

        return total
