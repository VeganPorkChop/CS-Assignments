"""
Author: YOUR NAME HERE
Starting Date: YOUR STARTING DATE HERE

An implementation of a Naive Bayes Classifier
"""

import math  # math.log()
import os
import pickle

"""
The name of positive dictionary cache file
"""
POSITIVE_DATA = "pos.dat"

"""
The name of negative dictionary cache file
"""
NEGATIVE_DATA = "neg.dat"

"""
The file name prefix for negative reviews
"""
NEGATIVE_FILE_PREFIX = "movies-1"

"""
The file name prefix for positive reviews
"""
POSITIVE_FILE_PREFIX = "movies-5"


class BayesClassifier:
    """A simple BayesClassifier implementation"""

    """
    A dictionary of frequencies of positive words
    """
    pos_freqs: dict[str, int]

    """
    A dictionary of frequencies of negative words
    """
    neg_freqs: dict[str, int]

    def __init__(self):
        """Constructor for the Naive Bayes Sentiment Classifier"""
        self.pos_freqs = {}
        self.neg_freqs = {}

    def setup(self, training_data: str):
        """
        If a cache of a trained classifier is stored in the current folder,
          it is loaded from that file;
        otherwise the system will proceed through training.

        Once setup, the classifier is ready to classify input text.

        Arguments:
            training_data: the local folder name with files to train on
        """
        if os.path.isfile(POSITIVE_DATA) and os.path.isfile(NEGATIVE_DATA):
            print("Data files found - loading to use cached values...")
            self.pos_freqs = self.load_dict(POSITIVE_DATA)
            self.neg_freqs = self.load_dict(NEGATIVE_DATA)
        else:
            print("Data files not found - running training...")
            self.train(training_data)
            self.save_dict(self.pos_freqs, POSITIVE_DATA)
            self.save_dict(self.neg_freqs, NEGATIVE_DATA)

    def save_dict(self, d: dict[str, int], filepath: str):
        """Pickle a given dictionary to a file with the given name.

        Args:
            d: A dictionary to pickle.
            filepath: The relative path to file to save.
        """
        print(f"Dictionary saved to file: {filepath}")
        with open(filepath, "wb") as f:
            pickle.Pickler(f).dump(d)

    def load_dict(self, filepath: str) -> dict[str, int]:
        """Load a pickled dictionary stored in given file.

        Args:
            filepath: The relative path to file to load.

        Returns:
            A dictionary stored in given file.
        """
        print(f"Loading dictionary from file: {filepath}")
        with open(filepath, "rb") as f:
            return pickle.Unpickler(f).load()  # type: ignore

    def load_file(self, filepath: str) -> str:
        """Load text of given file.

        Args:
            filepath: The relative path to file to load.

        Returns:
            The text of the given file.
        """
        with open(filepath, "r", encoding="utf8") as f:
            return f.read()

    def update_dict(self, words: list[str], freqs: dict[str, int]):
        """Update a given (word -> frequency) dictionary with given words list

        That is, increment the count of each word in words in the dictionary
        If any word in words is not currently in the dictionary,
          it is added with an initial count of 1

        Args:
            words: The list of tokens to update frequencies of
            freqs: A dictionary of frequencies to update
        """
        for word in words:
            freqs.setdefault(word, 0)
            freqs[word] +=1
        return

    def tokenize(self, text: str) -> list[str]:
        """Split the given text into a list of the individual tokens in order

        Specifically, tokens consist of lowercase letters, digits, and the symbols ', -, and _
          such that each word in the text is a distinct string in the output list

        Words are considered to be separated by _any_ non-tokenized characters

        For example,
        tokenize('Hello World 1234-5678') -> ['hello', 'world', '1234-5678']

        Args:
            text: The text to tokenize

        Returns:
            The tokens of given text in order
        """
        return text.lower().split()

    def train(self, training_data: str):
        """Train the Naive Bayes Sentiment Classifier

        Specifically, generate the `pos_freq/neg_freq` dictionaries
          with frequencies of words in corresponding positive/negative reviews

        Arguments:
            training_data: the local folder name with files to train on
        """
        # get the list of file names from the training data directory
        # os.walk returns a generator, of which we only need the first value
        _, _, files = next(os.walk(training_data), (None, None, []))
        if not files:
            raise RuntimeError(f"Couldn't find path {training_data}")
        print(training_data)
        this = self.load_file(training_data)
        print(this)
        # HINT: you may use the "files" list built above
        #       (try printing it out with a test case if you're not sure what's inside)
        # HINT: consider using some of the methods defined above, including load_file
        # HINT: training_data contains the folder name, you may want to combine it
        #       with each file using os.path.join(...)
        #       for example, os.path.join('a', 'b') gives the string 'a/b'

        # NOTE: training can take a while, we suggest printing out "progress reports"
        #       when you're looping over files in this function.
        #       Note that you can print things out without breaking test cases

        return

    def classify(self, text: str) -> str:
        """Classify the given text as negative or positive

        This is done by calculating the most likely document class
          as described in the lab writeup
          and using the pos_freqs and neg_freqs dictionaries associated with this classifier

        If either dictionary is empty (i.e., this classifier is untrained)
          then the behavior of this function is unspecified (anything can happen)

        Args:
            text: The text to classify

        Returns:
            The classification string, either 'positive' or 'negative'
        """
        # TODO: Implement me!

        # NOTE: remember that you need to tokenize as usual
        # NOTE: remember that we should add 1 to pos_count and neg_count before taking log
        # NOTE: some strings may not be in self.pos_freqs or self.neg_freqs

        # Hint: don't overthink the logic of this function
        #       it's pretty simple, and the trickiness is all in calculating the probabilities

        # Hint: remember to test this function using main.py,
        #       otherwise you may end up failing some hidden test cases...

        return ''
