from typing import Sequence

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download("punkt")

languages = {"ru": "russian", "eng": "english"}


def tokenize_by_words(sentence: str, lang: str = "ru") -> Sequence[str]:
    return word_tokenize(sentence, language=languages.get(lang))


def tokenize_by_sentence(text: str, lang: str = "ru") -> Sequence[str]:
    return sent_tokenize(text, language=languages.get(lang))
