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
    """
    This is the main method.
    """
    dictionary = "data/wordList.txt"
    essay = "data/englishEssay.txt"
    checker = SpellChecker(dictionary)
    print("Dictionary: " + dictionary)
    print("Essay to check: " + essay)
    wrong_words = checker.spell_check(essay)

    start = time.perf_counter()
    word_corrections = checker.spell_check(essay, suggest=True)
    end = time.perf_counter()
    elapsed = end - start
    print(f"Time to spellcheck: {elapsed:.3f}")

    for word in wrong_words:
        print(word)
    print()
    print("Suggested Corrections:")
    for word in word_corrections:
        print(word)


def test_code():
    """
    This method has some test code to test the project.
    """
    checker = SpellChecker("data/wordList.txt")

    print(WordInfo("blah", 3, 2))
    print(WordInfo("opportuantees", 10, 10))

    wrong_words = checker.spell_check("data/englishEssay.txt")
    print(wrong_words)
    for word in wrong_words:
        print(checker.suggest_mismisspellings(word, max=6))

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
