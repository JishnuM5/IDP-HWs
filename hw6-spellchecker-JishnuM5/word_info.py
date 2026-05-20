"""
Jishnu Mehta
Intermediate Data Programming Period 1
Spell Checker Project
"""


class WordInfo:
    """
    This class stores information about a misspelled word.
    """

    def __init__(self, misspelled, line, word_number, suggestions=None):
        """
        This will store the misspelled word, the line number, and the word number.
        If suggestions is not None, then it will store a list of suggestions.
        """
        self._misspelled = misspelled
        self._line = line
        self._word_number = word_number
        self._suggestions = suggestions

    # This is a required getter for Unit Tests to run
    def get_word(self):
        """
        This method returns the misspelled word.
        """
        return self._misspelled

    def __str__(self):
        """
        This method returns a string representation of the WordInfo object.
        """
        if (self._suggestions is None):
            return f"{self._misspelled:>15}:  line: {self._line:>3} word: {self._word_number:>2}"
        else:
            return (f"{self._misspelled:<14}--> {self._suggestions}")