from dataclasses import dataclass


@dataclass
class Vectorizer:
    def fit(self, training_data: list[str]): ...

    def transform(self, sentence: str) -> tuple[int]: ...
