from typing import Sequence

import pymorphy2

morph = pymorphy2.MorphAnalyzer()


def lemmatize(words: Sequence[str]) -> Sequence[str]:
    return [morph.parse(word)[0].normal_form for word in words]
