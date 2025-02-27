# Vectorize Words in a Sentence

- Problem: [problem.py](problem.py) _(create this file)_
- Template: [template.py](template.py) _(copy starter code from here)_
- Tests: [test_all.py](test_all.py) _(tests that verify your solution)_
- Solution: [solution.py](solution.py) _(our solution)_

**_Note: The [problem.py](problem.py) doesn't exist yet! After clicking the link above, click "Create File"._**

Large language models and other neural network models typically require input data to be in the form of a vector. In this problem, we will implement an object that turns words in a sentence into a vector.

Here's how your vectorizer will be used. First, we have the training data, which is a list of sentences. You can assume there won't be any punctuation.

```python
training_data = [
  "this is some training data"
]
```

You will then fit your vectorizer to the training data:

```python
vectorizer = Vectorizer()
vectorizer.fit(training_data)
```

Once fit, you can use your vectorizer to transform a sentence into a vector:

```python
vectorizer.transform("this is test data")
```

The output vector should be a tuple of 0s and 1s. When you fit your data, your vectorizer should uniquely assign words in alphabetical order to the positions in the vector. When you transform a sentence, each position in the output vector should be 1 if the word corresponding to the position is in the sentence, otherwise 0. If the sentence contains words that do not correspond to a position in the vector, the word should be ignored.

So, in this example, the output would be:

```
(1, 1, 0, 1, 0)
 ^  ^  ^  ^  ^-- training
 |  |  |  \----- this
 |  |  \-------- some
 |  \----------- is
 \-------------- data
```

Our training data was the sentence `"this is some training data"`. So our output vector would be of length 5 because there are 5 unique words. And each position in the output vector would correspond to `("data", "is", "some", "this", "training")` as these are the unique words from the sentence in alphabetical order. Finally, when we transform the sentence `"this is test data"`, the words `"this"`, `"is"`, and `"data"` are present and therefore have the value 1. `"some"` and `"training"` are not, and therefore have the value 0. And the word `"test"` is not present in the training data, so it not expressed in the output vector.

> **_Hint: Add this to the bottom of your problem.py file to run your code with your own input!_**
>
> ```python
> if __name__ == "__main__":
>     vectorizer = Vectorizer()
>     vectorizer.fit(["test training data"])
>     result = vectorizer.transform("data to transform")
>     print(result)
> ```
>
> With this main block, you can run your script by clicking the play button in the top right of VS Code.

Next up: [Problem p1322 - Summary Statistics of a Column in List of Dictionaries](../p1322/index.md)
