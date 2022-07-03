from turtle import title
import unittest
from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("Running up that hill", "Kate Bush")

    def test_song_has_title(self):
        self.assertEqual("Running up that hill", self.song_1.title)

    def test_song_has_artist(self):
        self.assertEqual("Kate Bush", self.song_1.artist)