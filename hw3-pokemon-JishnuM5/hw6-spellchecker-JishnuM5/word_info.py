"""
Jishnu Mehta
Intermediate Data Programming Period 1
Spell Checker Project
"""


class WordInfo:

    def __init__(self, misspelled, line, word_number, suggestions=None):
        self._misspelled = misspelled
        self._line = line
        self._word_number = word_number
        self._suggestions = suggestions

    # This is a required getter for Unit Tests to run
    def get_word(self):
        return self._misspelled

    # TODO: Add more getters & setters as necessary

    def __str__(self):
        return f"{self._misspelled:>13}: line: {self._line:>3} word: {self._word_number:>2}"
        # TODO: update to "print" the information nicely
        return self._misspelled
