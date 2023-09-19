import ast
import re

import nltk
from nltk import WordPunctTokenizer
from num2words import num2words

nltk.download("punkt")

word_punct_tokenizer = WordPunctTokenizer()


def normalize(text: str) -> str:
    text = _convert_to_lower_case(text)
    text = _delete_punctuation(text)
    text = _convert_digits_to_word(text)
    return text


def _convert_to_lower_case(text: str) -> str:
    return text.lower()


def _delete_punctuation(text: str) -> str:
    return " ".join(
        [
            word
            for word in word_punct_tokenizer.tokenize(text)
            if word.isalpha() or word.isalnum()
        ]
    )


def _convert_digits_to_word(text: str) -> str:
    pattern = r"\d+"
    numbers = re.findall(pattern, text)
    for number in numbers:
        text = text.replace(number, num2words(ast.literal_eval(number), lang="ru"))
    return text
