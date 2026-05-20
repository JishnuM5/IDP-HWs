"""
Jishnu Mehta
Intermediate Data Programming - Period 1
Tests the  functions of HW3
"""


import pandas as pd

from cse163_utils import assert_equals, parse

import hw3_manual
import hw3_pandas


# Write your test functions here!
def test_species_count(mnl, pds):
    """
    Tests the species_count method.
    """
    assert_equals(3, hw3_manual.species_count(mnl['poke_t']))
    assert_equals(3, hw3_pandas.species_count(pds['poke_t']))

    # My test cases
    assert_equals(5, hw3_manual.species_count(mnl['poke_t2']))
    assert_equals(5, hw3_pandas.species_count(pds['poke_t2']))
    # Edge cases
    assert_equals(1, hw3_manual.species_count(mnl['dupes']))
    assert_equals(1, hw3_pandas.species_count(pds['dupes']))
    assert_equals(1, hw3_manual.species_count(mnl['single']))
    assert_equals(1, hw3_pandas.species_count(pds['single']))
    assert_equals(0, hw3_manual.species_count(mnl['empty']))
    assert_equals(0, hw3_pandas.species_count(pds['empty']))


def test_max_level(mnl, pds):
    '''
    Tests the max_level method.

    '''
    assert_equals(('Lapras', 72), hw3_manual.max_level(mnl['poke_t']))
    assert_equals(('Lapras', 72), hw3_pandas.max_level(pds['poke_t']))

    # My test cases, which are all edge cases
    assert_equals(('Arcanine', 35), hw3_manual.max_level(mnl['single']))
    assert_equals(('Arcanine', 35), hw3_pandas.max_level(pds['single']))
    # The below cases test for handling multiple instances of max
    assert_equals(('Victreebel', 100), hw3_manual.max_level(mnl['poke_t2']))
    assert_equals(('Victreebel', 100), hw3_pandas.max_level(pds['poke_t2']))
    assert_equals(('Arcanine', 35), hw3_manual.max_level(mnl['dupes']))
    assert_equals(('Arcanine', 35), hw3_pandas.max_level(pds['dupes']))


def test_filter_range(mnl, pds):
    '''
    Tests the filter_range method.
    '''
    assert_equals(['Arcanine', 'Arcanine', 'Starmie'], hw3_manual.filter_range(mnl['poke_t'], 35, 72))
    assert_equals(['Arcanine', 'Arcanine', 'Starmie'], hw3_pandas.filter_range(pds['poke_t'], 35, 72))

    # My test cases, including edge cases
    assert_equals(['Gyarados', 'Dewgong'], hw3_manual.filter_range(mnl['poke_t2'], 35, 72))
    assert_equals(['Gyarados', 'Dewgong'], hw3_pandas.filter_range(pds['poke_t2'], 35, 72))
    assert_equals(['Arcanine'], hw3_manual.filter_range(mnl['single'], 35, 72))
    assert_equals(['Arcanine'], hw3_pandas.filter_range(pds['single'], 35, 72))
    assert_equals(['Arcanine', 'Arcanine', 'Arcanine', 'Arcanine', 'Arcanine'],
                  hw3_manual.filter_range(mnl['dupes'], 35, 72))
    assert_equals(['Arcanine', 'Arcanine', 'Arcanine', 'Arcanine', 'Arcanine'],
                  hw3_pandas.filter_range(pds['dupes'], 35, 72))
    # The below edge cases test for when no Pokemon fit the given parameters
    assert_equals([], hw3_manual.filter_range(mnl['poke_t'], 72, 35))
    assert_equals([], hw3_pandas.filter_range(pds['poke_t'], 72, 35))
    assert_equals([], hw3_manual.filter_range(mnl['empty'], 35, 72))
    assert_equals([], hw3_pandas.filter_range(pds['empty'], 35, 72))


def test_mean_attack_for_type(mnl, pds):
    '''
    Tests the mean_attack_for_type method.
    '''
    assert_equals(47.5, hw3_manual.mean_attack_for_type(mnl['poke_t'], 'fire'))
    assert_equals(47.5, hw3_pandas.mean_attack_for_type(pds['poke_t'], 'fire'))

    # My test cases, including edge cases
    assert_equals(137, hw3_manual.mean_attack_for_type(mnl['poke_t2'], 'water'))
    assert_equals(137, hw3_pandas.mean_attack_for_type(pds['poke_t2'], 'water'))
    assert_equals(50, hw3_manual.mean_attack_for_type(mnl['single'], 'fire'))
    assert_equals(50, hw3_pandas.mean_attack_for_type(pds['single'], 'fire'))
    assert_equals(50, hw3_manual.mean_attack_for_type(mnl['dupes'], 'fire'))
    assert_equals(50, hw3_pandas.mean_attack_for_type(pds['dupes'], 'fire'))
    # The below edge cases test for when no Pokemon fit the given type
    assert_equals(None, hw3_manual.mean_attack_for_type(mnl['poke_t2'], 'fire'))
    assert_equals(None, hw3_pandas.mean_attack_for_type(pds['poke_t2'], 'fire'))
    assert_equals(None, hw3_manual.mean_attack_for_type(mnl['empty'], 'fire'))
    assert_equals(None, hw3_pandas.mean_attack_for_type(pds['empty'], 'fire'))


def test_count_types(mnl, pds):
    '''
    Tests the count_types method.
    '''
    assert_equals({'fire': 2, 'water': 2}, hw3_manual.count_types(mnl['poke_t']))
    assert_equals({'fire': 2, 'water': 2}, hw3_pandas.count_types(pds['poke_t']))

    # My test cases, including edge cases
    assert_equals({'water': 3, 'ground': 1, 'grass': 1, 'poison': 1},
                  hw3_manual.count_types(mnl['poke_t2']))
    assert_equals({'water': 3, 'ground': 1, 'grass': 1, 'poison': 1},
                  hw3_pandas.count_types(pds['poke_t2']))
    assert_equals({'fire': 5}, hw3_manual.count_types(mnl['dupes']))
    assert_equals({'fire': 5}, hw3_pandas.count_types(pds['dupes']))
    assert_equals({'fire': 1}, hw3_manual.count_types(mnl['single']))
    assert_equals({'fire': 1}, hw3_pandas.count_types(pds['single']))
    assert_equals({}, hw3_manual.count_types(mnl['empty']))
    assert_equals({}, hw3_pandas.count_types(pds['empty']))


def test_mean_attack_per_type(mnl, pds):
    '''
    Tests the mean_attack_per_type method.
    '''
    assert_equals({'fire': 47.5, 'water': 140.5}, hw3_manual.mean_attack_per_type(mnl['poke_t']))
    assert_equals({'fire': 47.5, 'water': 140.5}, hw3_pandas.mean_attack_per_type(pds['poke_t']))

    # My test cases, including edge cases
    assert_equals({'water': 137.0, 'ground': 103.0, 'grass': 185.0, 'poison': 147.0},
                  hw3_manual.mean_attack_per_type(mnl['poke_t2']))
    assert_equals({'water': 137.0, 'ground': 103.0, 'grass': 185.0, 'poison': 147.0},
                  hw3_pandas.mean_attack_per_type(pds['poke_t2']))
    assert_equals({'fire': 50}, hw3_manual.mean_attack_per_type(mnl['single']))
    assert_equals({'fire': 50}, hw3_pandas.mean_attack_per_type(pds['single']))
    assert_equals({'fire': 50}, hw3_manual.mean_attack_per_type(mnl['dupes']))
    assert_equals({'fire': 50}, hw3_pandas.mean_attack_per_type(pds['dupes']))
    assert_equals({}, hw3_manual.mean_attack_per_type(mnl['empty']))
    assert_equals({}, hw3_pandas.mean_attack_per_type(pds['empty']))


def main():
    """
    This method runs all test code.
    """
    mnl = {
        "poke": parse("test/pokemon_box.csv"),
        "poke_t": parse("test/pokemon_test.csv"),
        "poke_t2": parse("test/pokemon_test2.csv"),
        "dupes": parse("test/duplicates.csv"),
        "single": parse("test/single.csv"),
        "empty": parse("test/empty.csv")
    }

    pds = {
        "poke": pd.read_csv("test/pokemon_box.csv"),
        "poke_t": pd.read_csv("test/pokemon_test.csv"),
        "poke_t2": pd.read_csv("test/pokemon_test2.csv"),
        "dupes": pd.read_csv("test/duplicates.csv"),
        "single": pd.read_csv("test/single.csv"),
        "empty": pd.read_csv("test/empty.csv"),
    }
    # Call your test functions here!
    test_species_count(mnl, pds)
    test_max_level(mnl, pds)
    test_filter_range(mnl, pds)
    test_mean_attack_for_type(mnl, pds)
    test_count_types(mnl, pds)
    test_mean_attack_per_type(mnl, pds)


if __name__ == '__main__':
    main()