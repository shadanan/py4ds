import os

if "PY4DS_PYTEST" in os.environ:
    from .solution import Vectorizer
else:
    from .problem import Vectorizer  # type: ignore


def test_instructions_example():
    vectorizer = Vectorizer()
    vectorizer.fit(["this is some training data"])
    actual = vectorizer.transform("this is test data")
    assert actual == (1, 1, 0, 1, 0)


def test_multiple_sentences():
    vectorizer = Vectorizer()
    vectorizer.fit(
        [
            "the black cat sleeps on the windowsill",
            "the black cat plays on the floor",
            "the brown dog sleeps on the carpet",
            "the dog plays with the cat",
            "a cat and dog run in the garden",
            "the garden has flowers and trees",
            "beautiful flowers grow in the garden",
            "trees provide shade in the garden",
        ]
    )
    actual = vectorizer.transform("the black dog runs on the floor near the garden")
    expected = (0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0)
    assert actual == expected
