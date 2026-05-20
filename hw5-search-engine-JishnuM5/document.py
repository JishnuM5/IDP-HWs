"""
Jishnu Mehta
Intermediate Data Programming
"""

from cse163_utils import normalize_token as nt
from cse163_utils import normalize_paths as np
import os


class Document:
    '''
    This class stores the important information for a single document.
    Given a path, it stores that path, the file contents, and various data about file content.
    '''

    def __init__(self, path, index=None):
        '''
        Initializes a new Document object. 
        If the given path is not a valid file, throws an exception.
        '''
        index = {} if index is None else index
        path = np(path)
        self._path = path
        self._name = os.path.basename(path)
        with open(self._path) as f:
            if f.read(1):
                f.seek(0)
                self._content = f.readlines()
            else:
                self._content = []
        self._word_count, self._term_dict = self._init_words(index)

    def _init_words(self, index):
        '''
        This method creates an initial index of word frequencies and the total number of words.
        I did not create a test method for this because it is part of initialization.
        Plus, all stored variables are tested for during other method testing.
        '''
        word_count = 0
        term_dict = {}
        for line in self._content:
            for word in line.split():
                word = nt(word)
                word_count += 1
                if word in term_dict.keys():
                    term_dict[word] += 1
                else:
                    term_dict[word] = 1
                    if word in index.keys():
                        index[word].append(self)
                    else:
                        index[word] = [self]
        return word_count, term_dict

    def get_path(self):
        '''
        This method returns the path of this document.
        '''
        return self._path

    def get_words(self):
        '''
        This method returns the unique, normalized set of words from this document.
        '''
        return list(self._term_dict.keys())

    def term_frequency(self, term):
        '''
        This method returns the term frequency in this document for a given term.
        '''
        if (self._word_count) == 0:
            return 0
        term = nt(term)
        term_count = self._term_dict[term] if term in self._term_dict.keys() else 0
        return term_count / self._word_count

    def __repr__(self):
        '''
        This method returns a string representation for a given method
        '''
        return self._name
