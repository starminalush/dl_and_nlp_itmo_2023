from typing import Sequence

import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")

stopwords_ru = set(stopwords.words("russian"))


def delete_stop_words(words: Sequence[str]) -> Sequence[str]:
    return [word for word in words if word not in stopwords_ru]
