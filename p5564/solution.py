from dataclasses import dataclass


@dataclass
class Vectorizer:
    def fit(self, training_data: list[str]):
        unique_words = set()
        for sentence in training_data:
            for word in sentence.split():
                unique_words.add(word)
        self.words = {word: index for index, word in enumerate(sorted(unique_words))}

    def transform(self, sentence: str) -> tuple[int, ...]:
        result = [0] * len(self.words)
        unique_words = set(sentence.split())
        for word in unique_words:
            if word in self.words:
                result[self.words[word]] = 1
        return tuple(result)
