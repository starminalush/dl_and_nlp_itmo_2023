from typing import Sequence

import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")

languages = {"ru": "russian", "eng": "english"}


def delete_stop_words(words: Sequence[str], lang: str = "ru") -> Sequence[str]:
    stopwords_ru = set(stopwords.words(languages.get(lang)))
    return [word for word in words if word not in stopwords_ru]
