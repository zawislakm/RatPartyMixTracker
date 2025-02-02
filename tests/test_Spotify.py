import unittest
import unittest.mock as mock
from unittest.mock import patch

from src.Database.models import Song
from src.ExternalAPIs import Spotify as Spotify


class TestSpotify(unittest.TestCase):

    @patch.dict('os.environ', {
        'CLIENT_ID': 'mock_client_id',
        'CLIENT_SECRET': 'mock_client_secret',
        'RAT_PARTY_MIX_ID': 'mock_rat_party_mix_id',
    })

    @mock.patch("requests.get")
    def test_get_song_by_id(self, mock_get):
        mock_response = mock.Mock()
        mock_response.json.return_value = {
            'name': 'test_song',
            'id': 'test_id',
            'artists': [{'id': 'test_artist_id', 'name': 'test_artist'}],
            'external_urls': {'spotify': 'test_link'},
            'album': {'images': [{'url': 'test_image_url'}]},
            'popularity': 50,
            'preview_url': 'test_preview_url'
        }
        mock_get.return_value = mock_response

        song = Spotify.get_song_by_id('test_id')
        self.assertIsInstance(song, Song)
        self.assertEqual(song.song_name, 'test_song')
        self.assertEqual(song.spotify_id, 'test_id')
        self.assertEqual(song.song_link, 'test_link')
        self.assertEqual(song.song_photo_link, 'test_image_url')
        self.assertEqual(song.popularity, 50)

    @mock.patch("requests.get")
    def test_get_playlist_description(self, mock_get):
        mock_response = mock.Mock()
        mock_response.json.return_value = {
            'description': 'test_description'
        }
        mock_get.return_value = mock_response

        description = Spotify.get_playlist_description()
        self.assertEqual(description, 'test_description')


if __name__ == '__main__':
    unittest.main()
