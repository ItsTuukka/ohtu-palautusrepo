import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )
    
    def test_loytaa_pelaajan(self):
        player = self.statistics.search("Semenko")

        self.assertAlmostEqual(str(player), "Semenko EDM 4 + 12 = 16")

    def test_ei_loyda_pelaajaa(self):
        player = self.statistics.search("tuukka")

        self.assertAlmostEqual(player, None)

    def test_haku_joukkueella(self):
        players = self.statistics.team("EDM")

        self.assertAlmostEqual(len(players), 3)

    def test_haku_eniten_pisteita(self):
        result = self.statistics.top(3)

        self.assertAlmostEqual(str(result[0]), "Gretzky EDM 35 + 89 = 124")
        self.assertAlmostEqual(len(result), 4)