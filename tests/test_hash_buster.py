import unittest
from unittest.mock import MagicMock, patch

from hash_buster import bruteforce_hash, wordlist_hash

class TestHashBuster(unittest.TestCase):
    def test_bruteforce_hash(self):
        mock_min = 1
        mock_max = 4
        
        mock_hash = 'fbc74209d6c21fd434df990c420af5f37b7f06b5252af4ddc2520159f54aca00'
        mock_hash_type = 'sha256'
        self.assertEqual(bruteforce_hash(mock_hash, mock_hash_type, mock_min, mock_max), 'c@t')

        mock_hash = '2b4ebdeaf66cf79cff3c4bc7e39c1e81'
        mock_hash_type = 'md5'
        self.assertEqual(bruteforce_hash(mock_hash, mock_hash_type, mock_min, mock_max), 'd0g')

        mock_min = 1
        mock_max = 2
        self.assertIsNone(bruteforce_hash(mock_hash, mock_hash_type, mock_min, mock_max))

    def test_wordlist_hash(self):
        file_path = '../rockyou.txt'

        mock_hash = '5ac2ac5ba94dbce933c6719ca250bf1752d938f43367af6618ab9e9e30b57df7' \
                    '01dcda95287c5af56d8374abf292813efa07e1f287b9e4877ff17969b6735fe1'
        mock_hash_type = 'sha512'
        self.assertEqual(wordlist_hash(mock_hash, mock_hash_type, file_path), 'p@ssw0rd')

        mock_hash ='113a0f181360317ccb0be347cfd75ae94e6d14e7b808af3c38765e18574da2cb' \
                   'ff18923f3a9795c72597e87011bf438eee7b8e526de8516d7154f08bd7750a03'
        mock_hash_type = 'BLAKE2b'
        self.assertEqual(wordlist_hash(mock_hash, mock_hash_type, file_path), 'strawberry')

        mock_hash = 'c157392770e70f58269186d1d8674f3f0b7981be'
        mock_hash_type = 'SHA1'
        self.assertIsNone(wordlist_hash(mock_hash, mock_hash_type, file_path))

