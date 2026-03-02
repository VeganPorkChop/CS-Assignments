"""
Author: YOUR NAME HERE
Starting Date: YOUR STARTING DATE HERE

A simple menu for training and inspecting
  the Naive Bayes Classifier implemented in lab6.py
"""

import lab6

"""
The relative path to training directory
"""
TRAINING_DATA_DIRECTORY = "movie_reviews/"


def inspect_probabilities(classifier: lab6.BayesClassifier):
    """Print probabilities for words for manual inspection.

    Arguments:
        classifier: A Naive Bayes classifier that has already been trained.
    """
    request = 'Give a single word to view probabilities of (or press Enter with no input to exit):\n'
    pos_denominator = sum(classifier.pos_freqs.values())
    neg_denominator = sum(classifier.neg_freqs.values())
    if pos_denominator == 0 or neg_denominator == 0:
        print("Classifier has no training data. This usually means either:")
        print("  1) The training directory (movie_reviews/) was missing or empty when you ran setup,")
        print("  2) Or pos.dat / neg.dat were saved from a failed run and are now cached empty.")
        print("Fix: Make sure movie_reviews/ exists in this folder and contains .txt review files.")
        print("     Then delete pos.dat and neg.dat (if they exist) and run main.py again.")
        return
    word = input(request)
    while word != '':
        print(f"P('{word}' | pos) = {(classifier.pos_freqs.get(word.lower(), -1)+1)/pos_denominator}")
        print(f"P('{word}' | neg) = {(classifier.neg_freqs.get(word.lower(), -1)+1)/neg_denominator}")
        word = input(request)
    print("Exiting the probability viewer")


def test_classifier(classifier: lab6.BayesClassifier):
    """Manually test how the classifier classifies sentences.

    Arguments:
        classifier: A Naive Bayes classifier that has already been trained.
    """
    request = 'Give a sentence to classify (or press Enter with no input to exit): '
    sentence = input(request)
    while sentence != '':
        result = classifier.classify(sentence)
        print(f'The classifier rates your sentence as {result}')
        sentence = input(request)
    print("Exiting the classifier")


def main():
    """Train the classifier if not already trained, then run the menu."""
    classifier = lab6.BayesClassifier()
    classifier.setup(TRAINING_DATA_DIRECTORY)
    choice = input('What should we do with our classifier?\n 1 to inspect probabilities\n 2 to classify text\n')
    if choice == '1':
        inspect_probabilities(classifier)
    elif choice == '2':
        test_classifier(classifier)
    else:
        print('Invalid option, quitting')


if __name__ == "__main__":
    main()
