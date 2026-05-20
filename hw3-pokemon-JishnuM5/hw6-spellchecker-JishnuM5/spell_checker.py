"""
Jishnu Mehta
Intermediate Data Programming Period 1
Spell Checker Project

Students must have a FAST implementation.
"""

import re
# from levenshtein import levenshtein_distance, lev_distance


class SpellChecker:

    def __init__(self, dictionary):
        """
        """
        # This is the list of all words in the given (actual, not data type) dictionary
        self._words = set()
        with open(dictionary) as f:
            for word in f.read().split():
                self._words.add(word)

    def spell_check(self, file_name):
        """
        This will check the spelling of every word in the file_name.
        It will return a list of WordInfo objects that describe the words misspelled.
        """
        pass

    def misspelled(self, word):
        """
        This method MUST deal with hyphenated words.
        If any part of a hyphenated word is misspelled, then the whole word
        is misspelled.

        word is not normalized and may or may not be hyphenated.
        return True if the word is misspelled, False if spelled correctly.
        """
        # normalize the word
        misspelled = False
        word = normalize_token(word)
        if '-' in word:
            for token in word.split('-'):
                # if true, return
                pass
        else:
            misspelled = word not in self._words
        # return True if misspelled
        return misspelled

    def suggest_corrections(self, word):
        """
        word : the misspelled word to find suggestions for

        Return a list of all the suggested words that share the same minimum
        distance from word using the levenshtein distance algorithm.
        """
        # Student must implement
        pass

    def suggest_mismisspellings(self, word, max=6):
        """
        word : the misspelled word to find suggestions for
        max : the max size of the list returned

        Return a list of all the suggested words by using the mis-misspelled
        approach. See instructions.
        """
        corrections = []
        # 1st nested loop: insert, delete, swap
        # 2nd nested loop: insert, swap, delete
        # 3rd nested loop: delete, insert, swap
        # 4th nested loop: delete, swap, insert
        # 5th nested loop: swap, insert, delete
        # 6th nested loop: swap, delete, insert

        # each time a word is added to corrections, return the list if len(corrections) == max
        return corrections

    def _insert_letters(self, word):
        """
        This is a generator that will insert a-z at all location in the word
        """
        yield word
        for i in range(len(word)):
            for letter in "abcdefghijklmnopqrstuvwxyz":
                yield word[:i] + letter + word[i:]

    def _remove_letters(self, word):
        """
        This is a generator that will remove each letter one at a time
        """
        yield word
        for i in range(len(word)):
            yield word[:i] + word[i + 1:]

    # from 'ettiquitt' to 'etiquette' is: remove t, add e, swap i with e.
    def _swap_letters(self, word):
        """
        This is a generator that will replace each letter with a-z.
        This is sort of like a composition of insert & remove letters
        """
        yield word
        for i in range(len(word)):
            for letter in "abcdefghijklmnopqrstuvwxyz":
                if letter != word[i]:
                    yield word[:i] + letter + word[i + 1:]


def normalize_token(token):
    """
    Removes non-alphabetic characters using a regular expression.
    Don't forget to handle upper vs lowercase letters. Let's go lowercase.
    The hyphen is NOT removed. It remains.
    """
    # student will NOT need to change
    return re.sub(r"[^A-Za-z\-]", "", token.lower())
