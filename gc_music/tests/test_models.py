from django.test import TestCase
from gc_music.models import Song

class TestModels(TestCase):
    @classmethod
    def setUpTestData(cls):
        Song.objects.create(songname='test song', songartist='test artist', songimg='test image')

    def test_song_name(self):
        testsong = Song.objects.get(id=1)
        song_name = testsong.songname
        self.assertEqual(song_name, 'test song')

    def test_song_artist(self):
        testsong = Song.objects.get(id=1)
        song_artist = testsong.songartist
        self.assertEqual(song_artist, 'test artist')