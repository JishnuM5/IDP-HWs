"""
Jishnu Mehta
Intermediate Data Programming
"""

# The tests you create will be graded

import math
from cse163_utils import assert_equals
from document import Document
from search_engine import SearchEngine


# This file is left blank for you to fill in with your tests!
def test_search_engine():
    '''
    This method runs all helper methods to test the SearchEngine class.
    '''
    engine = SearchEngine("hw5_test_corpus")
    test_calculate_idf(engine)
    test_search(engine)


def test_calculate_idf(engine):
    '''
    This method tests the _calculate_idf method in the SearchEngine class
    '''
    # I am not testing any un-normalized tokens here because this tests a private method
    # _calculate_idf method is only called from search, which normalizes tokens before passing them on

    # A normal test case for a word appearing in 3 documents
    assert_equals(math.log(5 / 3), engine._calculate_idf("to"))
    # A normal test case for a word appearing in 1 document
    assert_equals(math.log(5 / 1), engine._calculate_idf("i"))
    # The edge case of an empty string
    assert_equals(0, engine._calculate_idf(""))
    # The edge case for a word not in any document
    assert_equals(0, engine._calculate_idf("not_a_term"))


def test_search(engine):
    '''
    This method tests the search method in the SearchEngine class
    '''
    # A normal test case for a term appearing in 3 documents
    assert_equals(['hw5_test_corpus/document3.txt', 'hw5_test_corpus/document1.txt',
                  'hw5_test_corpus/long_word.txt'], engine.search("to"))
    # A normal test case for a term appearing in 1 document
    assert_equals(['hw5_test_corpus/document1.txt'], engine.search("i"))
    # A normal test case for a multi-word query
    assert_equals(['hw5_test_corpus/document1.txt', 'hw5_test_corpus/document3.txt',
                  'hw5_test_corpus/long_word.txt'], engine.search("i to"))
    # An edge case for an un-normalized query
    assert_equals(['hw5_test_corpus/document1.txt', 'hw5_test_corpus/long_word.txt'],
                  engine.search("I!! (sometimes)"))
    # The edge case of an empty string
    assert_equals([], engine.search(""))
    # The edge case for a query with words not in any document
    assert_equals([], engine.search("not_a_term neither_this_one"))


def test_document():
    '''
    This method runs all helper methods to test the Document class.
    '''
    d1 = Document("hw5_test_corpus/document1.txt")
    d2 = Document("hw5_test_corpus/document2.txt")
    d3 = Document("hw5_test_corpus/document3.txt")
    long = Document("hw5_test_corpus/long_word.txt")
    empty = Document("hw5_test_corpus/empty.txt")

    test_doc_get_words(d1, d2, d3, empty)
    test_doc_term_frequency(d1, d2, d3, long, empty)
    test_doc_get_path(d1, d2, empty)


def test_doc_get_words(d1, d2, d3, empty):
    '''
    This method tests the get_words method in the Document class
    '''
    # A document with a multiple un-normalized tokens
    assert_equals(sorted(["i", "love", "programming", "however", "have", "to", "admitit",
                  "drives", "me", "crazy", "sometimes"]), sorted(d1.get_words()))
    # The edge case for a file with a single word
    assert_equals(sorted(["single"]), sorted(d2.get_words()))
    # A normal test case
    assert_equals(sorted(["all", "the", "words", "are", "echoing", "to",
                  "ooooooooooh", "aaaaaaaaaah"]), sorted(d3.get_words()))
    # The edge case for an empty file
    assert_equals([], empty.get_words())


def test_doc_term_frequency(d1, d2, d3, long, empty):
    '''
    This method tests the term_frequency method in the Document class
    '''
    # The edge case of an un-normalized token whose normalized version exists in the file
    assert_equals(2 / 12, d1.term_frequency("I!!!"))
    # The edge case for a single-word file
    assert_equals(1, d2.term_frequency("single"))
    # The edge case for a term not in the file
    assert_equals(0, d3.term_frequency("word"))
    # For this normal test case, I used an online word counter
    assert_equals(36 / 504, long.term_frequency("the"))
    # The edge case for an empty file
    assert_equals(0, empty.term_frequency("pneumonoultramicroscopicsilicovolcanoconiosis"))


def test_doc_get_path(d1, d2, empty):
    '''
    This method tests the get_path method in the Document class
    '''
    # Normal test case #1
    assert_equals("hw5_test_corpus/document1.txt", d1.get_path())
    # Normal test case #2
    assert_equals("hw5_test_corpus/document2.txt", d2.get_path())
    # The possible edge case of an empty file
    assert_equals("hw5_test_corpus/empty.txt", empty.get_path())


def main():
    '''
    This method runs all tests methods
    '''
    test_document()
    test_search_engine()


if __name__ == '__main__':
    main()