"""
Jishnu Mehta
Intermediate Data Programming Period 1
Spell Checker Project

Students must have a FAST implementation.
"""

import re
from levenshtein import lev_distance
import itertools
from word_info import WordInfo


class SpellChecker:
    """
    This class can spell check a file and suggest corrections.
    """

    def __init__(self, dictionary_name):
        """
        This will read in the dictionary file and store the words in a set.
        """
        self._words = set()
        with open(dictionary_name) as f:
            for word in f.read().split():
                self._words.add(word)

    def spell_check(self, file_name, suggest=False):
        """
        This will check the spelling of every word in the file_name.
        It will return a list of WordInfo objects that describe the words misspelled.
        If suggest is True, then the WordInfo object will also contain a list of suggestions.
        """
        misspellings = []
        with open(file_name) as f:
            line_count = 0
            for line in f.readlines():
                line_count += 1
                word_count = 0
                for word in line.split():
                    word = normalize_token(word)
                    word_count += 1
                    if self.misspelled(word):
                        if (suggest):
                            suggestions = self.suggest_corrections(word)
                            misspellings.append(WordInfo(word, line_count, word_count, suggestions))
                        else:
                            misspellings.append(WordInfo(word, line_count, word_count))
        return misspellings

    def misspelled(self, word):
        """
        This method MUST deal with hyphenated words.
        If any part of a hyphenated word is misspelled, then the whole word
        is misspelled.

        The given word is not normalized and may or may not be hyphenated.
        The method returns True if the word is misspelled, False if spelled correctly.
        """        
        word = normalize_token(word)
        if '-' in word:
            for token in word.split('-'):
                if self.misspelled(token):
                    return True
        elif word not in self._words:
            return True
        return False

    def suggest_corrections(self, word):
        """
        The `word` parameter is the misspelled word to find suggestions for.

        This method returns a list of all the suggested words that share the same
        minimum distance from word using the levenshtein distance algorithm.
        """
        word = normalize_token(word)
        sub_words = word.split('-')
        corrections = {}
        corrections_list = []

        for sub_word in sub_words:
            min_distance = float('inf')
            for correct_word in self._words:
                distance = lev_distance(sub_word, correct_word)
                if distance < min_distance:
                    corrections[sub_word] = [correct_word]
                    min_distance = distance
                elif distance == min_distance:
                    corrections[sub_word].append(correct_word)

        # Generate all possible combinations of the correct words
        # The `*` symbol unpacks the list of lists into the function
        for combination in itertools.product(*corrections.values()):
            corrections_list.append('-'.join(combination))
        return corrections_list

    def suggest_mismisspellings(self, word, max=6):
        """
        The `word` parameter the misspelled word to find suggestions for.
        The `max` parameter is the max size of the list returned.

        The method returns a list of all the suggested words by using the 
        mis-misspelled approach. See instructions.
        """
        corrections = []
        word = normalize_token(word)
        # 1st nested loop: insert, delete, swap
        for inserted_word in self._insert_letters(word):
            for deleted_word in self._remove_letters(inserted_word):
                for swapped_word in self._swap_letters(deleted_word):
                    if not self.misspelled(swapped_word):
                        corrections.append(swapped_word)
                        if len(corrections) == max:
                            return corrections
        # 2nd nested loop: insert, swap, delete
        for inserted_word in self._insert_letters(word):
            for swapped_word in self._swap_letters(inserted_word):
                for deleted_word in self._remove_letters(swapped_word):
                    if not self.misspelled(deleted_word):
                        corrections.append(deleted_word)
                        if len(corrections) == max:
                            return corrections
        # 3rd nested loop: delete, insert, swap
        for deleted_word in self._remove_letters(word):
            for inserted_word in self._insert_letters(deleted_word):
                for swapped_word in self._swap_letters(inserted_word):
                    if not self.misspelled(swapped_word):
                        corrections.append(swapped_word)
                        if len(corrections) == max:
                            return corrections
        # 4th nested loop: delete, swap, insert
        for deleted_word in self._remove_letters(word):
            for swapped_word in self._swap_letters(deleted_word):
                for inserted_word in self._insert_letters(swapped_word):
                    if not self.misspelled(inserted_word):
                        corrections.append(inserted_word)
                        if len(corrections) == max:
                            return corrections
        # 5th nested loop: swap, insert, delete
        for swapped_word in self._swap_letters(word):
            for inserted_word in self._insert_letters(swapped_word):
                for deleted_word in self._remove_letters(inserted_word):
                    if not self.misspelled(deleted_word):
                        corrections.append(deleted_word)
                        if len(corrections) == max:
                            return corrections
        # 6th nested loop: swap, delete, insert
        for swapped_word in self._swap_letters(word):
            for deleted_word in self._remove_letters(swapped_word):
                for inserted_word in self._insert_letters(deleted_word):
                    if not self.misspelled(inserted_word):
                        corrections.append(inserted_word)
                        if len(corrections) == max:
                            return corrections
        return corrections

    def _insert_letters(self, word):
        """
        This is a generator that will insert a-z at all locations in the word.
        """
        yield word
        for i in range(len(word) + 1):
            for letter in "abcdefghijklmnopqrstuvwxyz":
                yield word[:i] + letter + word[i:]

    def _remove_letters(self, word):
        """
        This is a generator that will remove each letter from the word one at a time.
        """
        yield word
        for i in range(len(word)):
            yield word[:i] + word[i + 1:]

    # from 'ettiquitt' to 'etiquette' is: remove t, add e, swap i with e.
    def _swap_letters(self, word):
        """
        This is a generator that will replace each letter with a-z.
        This is sort of like a composition of insert & remove letters.
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
