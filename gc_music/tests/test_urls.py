from django.test import TestCase, Client
from gc_music.models import Song

class TestUrls(TestCase):
    @classmethod
    def setUpTestData(cls):
        Song.objects.create(songname='test song', songartist='test artist', songimg='test image')
        Song.objects.create(songname='test song 2', songartist='test artist 2', songimg='test image 2')

    def test_main(self):
        c = Client()
        res = c.get('/')
        print(res.content)
        self.assertEqual(res.status_code, 200)
    
    def test_songs(self):
        c = Client()
        res = c.get('/songs')
        print(res.content)
        self.assertEqual(res.status_code, 200)
    
    def test_song(self):
        c = Client()
        res = c.get('/song/3')
        print(res.content)
        self.assertEqual(res.status_code, 200)

    def test_new_song(self):
        c = Client()
        data = {
            "songname": "new Song",
            "songartist": "New Song Artist",
            "songimg": 'New Song Img'
        }

        res = c.post('/new_song', data)
        self.assertEqual(res.status_code, 200)


