import unittest
import unittest.mock as mock

from src.Database.models import Song, Artist
from src.ExternalAPIs.Twitter import read_photo, remove_photo, get_songs_string, make_tweet


class TestTwitter(unittest.TestCase):

    @mock.patch('requests.get')
    def test_read_photo_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.__iter__.return_value = (b'chunk1', b'chunk2')

        result = read_photo('http://example.com/photo.jpg')
        self.assertTrue(result)
        remove_photo()

    @mock.patch('requests.get')
    def test_read_photo_failure(self, mock_get):
        mock_get.return_value.status_code = 404
        result = read_photo('http://example.com/photo.jpg')
        self.assertFalse(result)

    def test_get_songs_string(self):
        song1 = Song({'name': 'test_song1', 'id': 'test_id1'})
        song2 = Song({'name': 'test_song2', 'id': 'test_id2'})

        artist1 = Artist({'name': 'test_artist1', 'id': 'test_artist_id1'})
        artist2 = Artist({'name': 'test_artist2', 'id': 'test_artist_id2'})

        song1.add_artist(artist1)
        song1.add_artist(artist2)
        song2.add_artist(artist1)

        songs = [song1, song2]

        result = get_songs_string(songs)
        self.assertEqual(result, 'test_song1 from test_artist1, test_artist2\ntest_song2 from test_artist1')

    @mock.patch("src.ExternalAPIs.Twitter.Client.create_tweet")
    @mock.patch("src.ExternalAPIs.Twitter.API.media_upload")
    @mock.patch("src.ExternalAPIs.Twitter.read_photo")
    def test_make_tweet(self, mock_read_photo, mock_media_upload, mock_create_tweet):
        mock_read_photo.return_value = True
        mock_media_upload.return_value = mock.Mock(media_id='test_media_id')
        make_tweet('test_text', 'test_url')
        mock_create_tweet.assert_called_with(text='test_text', media_ids=['test_media_id'])


if __name__ == '__main__':
    unittest.main()
