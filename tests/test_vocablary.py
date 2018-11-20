import unittest

from pathlib import Path

from sanascan_backend.lang_model import LangModel
from sanascan_backend.vocabulary import Vocabulary
from sanascan_backend.word import TagWord
from sanascan_backend.key import Key


class TestVocabulary(unittest.TestCase):
    def setUp(self) -> None:
        with (Path.home() / 'arpa/LM0006.txt').open() as f:
            lm = LangModel(f.read())
        self.vocab = Vocabulary(lm.get_vocab())
        self.key = Key([3, 1, 4, TagWord('<num>')])
        self.keys = [
            Key([TagWord('<num>')]),
            Key([4, TagWord('<num>')]),
            Key([1, 4, TagWord('<num>')]),
            Key([3, 1, 4, TagWord('<num>')]),
        ]

    # このテストが通らないことが致命的
    def test_have_num_tagwotd(self) -> None:
        self.assertIn(TagWord('<num>'), self.vocab._datum.keys())

    def test_get_by_key(self) -> None:
        list(self.vocab.get_by_key(self.key, 3))
        for word, key in self.vocab.get_by_key(self.key, 3):
            print()
            print(key)
            print()
            self.assertIn(key, self.keys)
