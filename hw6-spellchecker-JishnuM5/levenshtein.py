"""
Jishnu Mehta
Intermediate Data Programming Period 1
Spell Checker Project
"""

# Find an Implementation of Levenshtein Distance on the internet.
# You should do this TWO ways:
# 1) python code (used in the method 'levenshtein_distance')
# 2) import a module (used in the method 'lev_distance')

# To import Levenshtein, you need: pip install python-Levenshtein
from Levenshtein import distance


def levenshtein_distance(s1, s2):
    """
    This is the internet code for the Levenshtein Distance.
    """
    # Find internet code to return the distance between s1 & s2
    m = len(s1)
    n = len(s2)
    d = [[0] * (n + 1) for i in range(m + 1)]  

    for i in range(1, m + 1):
        d[i][0] = i

    for j in range(1, n + 1):
        d[0][j] = j

    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                cost = 0
            else:
                cost = 1
            d[i][j] = min(d[i - 1][j] + 1,
                          d[i][j - 1] + 1,
                          d[i - 1][j - 1] + cost)
    return d[m][n]


def lev_distance(s1, s2):
    """
    This method implements the Levenshtein module.
    """
    # This is a wrapper method that calls the module's implementation
    return distance(s1, s2)