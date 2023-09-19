from typing import Sequence

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download('punkt')


def tokenize_by_words(sentence: str) -> Sequence[str]:
    return word_tokenize(sentence, language="russian")


def tokenize_by_sentence(text: str) -> Sequence[str]:
    return sent_tokenize(text, language="russian")
