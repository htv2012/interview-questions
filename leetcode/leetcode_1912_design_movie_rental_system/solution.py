import bisect
from typing import List


class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        self.price_lookup = {}
        self.in_stock = {}
        self.rented = []
        for shop, movie, price in entries:
            stock = self.in_stock.setdefault(movie, [])
            bisect.insort(stock, (price, shop))
            self.price_lookup[shop, movie] = price

    def search(self, movie: int) -> List[int]:
        stock = self.in_stock.get(movie, [])
        return [shop for price, shop in stock[:5]]

    def rent(self, shop: int, movie: int) -> None:
        price = self.price_lookup[shop, movie]
        self.in_stock[movie].remove((price, shop))
        bisect.insort(self.rented, (price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.price_lookup[shop, movie]
        self.rented.remove((price, shop, movie))
        bisect.insort(self.in_stock[movie], (price, shop))

    def report(self) -> List[List[int]]:
        return [[shop, movie] for _, shop, movie in self.rented[:5]]


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
