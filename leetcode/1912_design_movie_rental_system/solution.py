import sqlite3
from typing import List

SQL_CREATE_TABLES = """
CREATE TABLE rental (
    shop INTEGER,
    movie INTEGER,
    price INTEGER,
    rented INTEGER DEFAULT 0
)
"""

SQL_ADD_ENTRY = """
INSERT INTO rental
(shop, movie, price) VALUES (?, ?, ?)
"""

SQL_SEARCH = """
SELECT shop
FROM rental
WHERE movie = ? AND rented = 0
ORDER BY price ASC, shop ASC
LIMIT 5
"""

SQL_RENT = """
UPDATE rental
SET rented = 1
WHERE shop = ? AND movie = ?
"""

SQL_DROP = """
UPDATE rental
SET rented = 0
WHERE shop = ? AND movie = ?
"""

SQL_REPORT = """
SELECT shop, movie FROM rental
WHERE rented = 1
ORDER BY price ASC, shop ASC, movie ASC
LIMIT 5
"""


class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        self.db = sqlite3.connect(":memory:")
        self.db.execute(SQL_CREATE_TABLES)

        # Add the entries
        self.db.executemany(SQL_ADD_ENTRY, entries)
        self.db.commit()

    def search(self, movie: int) -> List[int]:
        """
        Finds the cheapest 5 shops that have an unrented copy of a given
        movie. The shops should be sorted by price in ascending order,
        and in case of a tie, the one with the smaller shopi should
        appear first. If there are less than 5 matching shops, then all
        of them should be returned. If no shop has an unrented copy,
        then an empty list should be returned.
        """
        shops = [record[0] for record in self.db.execute(SQL_SEARCH, (movie,))]
        return shops

    def rent(self, shop: int, movie: int) -> None:
        self.db.execute(SQL_RENT, (shop, movie))
        self.db.commit()

    def drop(self, shop: int, movie: int) -> None:
        self.db.execute(SQL_DROP, (shop, movie))
        self.db.commit()

    def report(self) -> List[List[int]]:
        """
        Returns the cheapest 5 rented movies (possibly of the same movie
        ID) as a 2D list res where res[j] = [shopj, moviej] describes that
        the jth cheapest rented movie moviej was rented from the shop
        shopj. The movies in res should be sorted by price in ascending
        order, and in case of a tie, the one with the smaller shopj
        should appear first, and if there is still tie, the one with the
        smaller moviej should appear first. If there are fewer than 5
        rented movies, then all of them should be returned. If no movies
        are currently being rented, then an empty list should be returned.
        """
        result = [list(record) for record in self.db.execute(SQL_REPORT)]
        return result
