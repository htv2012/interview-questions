import unittest

from player import Player


class Smoke(unittest.TestCase):
	def setUp(self):
		self.player = Player("John")

	def test_has_shoot(self):
		self.player.shoot

	def test_has_assess(self):
		self.player.assess

	def test_add_ship(self):
		self.player.add_ship("A1", "B1")


class Functional(unittest.TestCase):
	def setUp(self):
		self.player = Player("John")


if __name__ == '__main__':
	unittest.main()