from typing import List


class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        raise NotImplementedError("__init__")

    def search(self, movie: int) -> List[int]:
        raise NotImplementedError("search")

    def rent(self, shop: int, movie: int) -> None:
        raise NotImplementedError("rent")

    def drop(self, shop: int, movie: int) -> None:
        raise NotImplementedError("drop")

    def report(self) -> List[List[int]]:
        raise NotImplementedError("report")


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
