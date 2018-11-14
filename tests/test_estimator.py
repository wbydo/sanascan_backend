import unittest
from pathlib import Path

from natto import MeCab

from sanascan_backend.estimator import estimate
from sanascan_backend.lang_model import LangModel
from sanascan_backend.key_to_word_map import KeyToWordMap
from sanascan_backend.word import Word


class TestEstimator(unittest.TestCase):
    def setUp(self) -> None:
        with (Path.home() / 'arpa/LM0006.txt').open() as f:
            self.lm = LangModel(f.read())

    def test_hoge(self) -> None:
        sentence = 'ホテル内の飲食店が充実しており、特に１Ｆのバーは重厚なインテリアで、雰囲気が良く最高'
        words = Word.from_sentence(sentence, MeCab())

        result = estimate(
            words,
            KeyToWordMap(self.lm.get_vocab()),
            self.lm,
            self.lm._order
        )
        print(result)


if __name__ == '__main__':
    unittest.main()
