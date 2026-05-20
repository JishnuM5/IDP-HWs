"""
Jishnu Mehta
Intermediate Data Programming Period 1
Spell Checker Project
"""

from spell_checker import SpellChecker
from word_info import WordInfo
from levenshtein import levenshtein_distance, lev_distance
import time


def main():
    start = time.perf_counter()

    # checker = SpellChecker("data/wordList.txt")
    test_code()

    end = time.perf_counter()
    elapsed = end - start
    print(f"Time to spellcheck: {elapsed:.3f}")


def test_code():
    checker = SpellChecker("data/wordSmall.txt")
    print(checker._words)
    print(WordInfo("blah", 3, 2))
    print(WordInfo("opportuantees", 10, 10))

    for word in checker._insert_letters("cat"):
        print(word)
    for word in checker._remove_letters("goodbye"):
        print(word)
    for word in checker._swap_letters("ab"):
        print(word)

    a = ['Mavs', 'Spurs', 'Lakers', 'Cavs']
    b = ['Rockets', 'Pacers', 'Warriors', 'Celtics']
    for i, k in zip(a, b):
        print("Without Library: ", levenshtein_distance(i, k))
        print("With Library: ", lev_distance(i, k))


if __name__ == "__main__":
    main()
