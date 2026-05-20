"""
Jishnu Mehta
Intermediate Data Programming - Period 1
Implements the functions for HW3 with pandas
"""

# Your code here!


def species_count(data):
    '''
    Takes a Pokemon DataFrame and returns the number of unique pokemon species (unique Pokemon names).
    '''
    if data.empty:
        return 0
    return len(data.groupby('name')['id'].count())


def max_level(data):
    '''
    Takes a Pokemon DataFrame and returns the a 2-element tuple of the (name, level) 
    of the Pokemon with the highest level. If duplicates present returns first instance.
    '''
    max = data['level'].max()
    idx = data['level'].idxmax()
    return data.loc[idx, 'name'], max


def filter_range(data, min, max):
    '''
    Takes a Pokemon DataFrame, a lower bound (inclusive) and upper bound (exclusive).
    Returns a list of Pokemon whose levels are within the bounds in the same order as the dataset.
    '''
    series = data[(data['level'] >= min) & (data['level'] < max)]['name']
    return list(series)


def mean_attack_for_type(data, type):
    '''
    Takes a Pokemon DataFrame and a Pokemon type string.
    Returns the average attack for all the Pokemon with the given type. 
    If no Pokemon of the type, returns None.
    '''
    df = data[data['type'] == type]['atk']
    if df.empty:
        return None
    else:
        return df.mean()


def count_types(data):
    '''
    Takes a Pokemon DataFrame and returns a dictionary with the number of Pokemon for each type.
    '''
    return dict(data.groupby('type')['name'].count())


def mean_attack_per_type(data):
    '''
    Takes a Pokemon DataFrame and returns a dictionary with the average attack of each type.
    '''
    print(data.groupby('type')['atk'].mean())
    return dict(data.groupby('type')['atk'].mean())