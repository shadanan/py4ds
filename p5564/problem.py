from dataclasses import dataclass


@dataclass
class Vectorizer:
    def fit(self, training_data: list[str]):
        pass

    def transform(self, sentence: str) -> tuple[int]:
        pass
