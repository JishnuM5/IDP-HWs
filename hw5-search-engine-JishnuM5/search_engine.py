"""
Jishnu Mehta
Intermediate Data Programming
"""

import math
import os
from document import Document
from cse163_utils import normalize_token as nt
from cse163_utils import normalize_paths as np


class SearchEngine:
    '''
    This class implements a search engine that stores information about all documents and their words.
    It creates an inverted index that, along with the Document class, is used to answer search queries
    '''

    def __init__(self, directory):
        '''
        Here, the SearchEngine class is initialized, creating references to all documents
        An inverted index and document count is also created
        '''
        directory = np(directory)
        self._docs = {}
        self._doc_count = 0
        self._inverted = {}
        for filename in os.listdir(os.path.join(os.getcwd(), directory)):
            self._doc_count += 1
            self._docs[filename] = Document(os.path.join(directory, filename), self._inverted)

    def _calculate_idf(self, term):
        '''
        Calculates` the IDF for a given string. If the term is not in the index, IDF is 0.
        '''
        if term not in self._inverted.keys():
            return 0

        return math.log(self._doc_count / len(self._inverted[term]))

    def search(self, query):
        '''
        Searches for the query in all documents, and returns a list based ordered by TF-IDF.
        Does not return documents that contain no query words (TF-IDF is zero).
        '''
        doc_tfidfs = {}
        for term in query.split():
            term = nt(term)
            term_idf = self._calculate_idf(term)
            if term_idf == 0:
                continue
            for doc in self._inverted[term]:
                path = doc.get_path()
                if path in doc_tfidfs:
                    doc_tfidfs[path] += term_idf * doc.term_frequency(term)
                else:
                    doc_tfidfs[path] = term_idf * doc.term_frequency(term)
        return sorted(doc_tfidfs.keys(), key=lambda key: doc_tfidfs[key], reverse=True)
