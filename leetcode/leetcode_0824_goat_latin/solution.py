VOWELS = set("aeiouAEIOU")


def transform_word(count_of_letter_a: int, word: str):
    if word[0] not in VOWELS:
        word = f"{word[1:]}{word[0]}"
    word = f"{word}ma{count_of_letter_a * 'a'}"
    return word


class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        return " ".join(
            transform_word(count, word)
            for count, word in enumerate(sentence.split(), 1)
        )
