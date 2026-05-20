# Your code here!
"""
Jishnu Mehta
Intermediate Data Programming - Period 1
Implements the functions for HW3 manually
"""


def species_count(data):
    '''
    Takes a Pokemon list of dictionaries and returns the number of unique pokemon species
    (unique Pokemon names).
    '''
    species = set()
    for item in data:
        species.add(item['name'])
    return len(species) 


def max_level(data):
    '''
    Takes a Pokemon list of dictionaries and returns the a 2-element tuple of the (name, level) 
    of the Pokemon with the highest level. If duplicates present returns first instance.
    '''
    max = data[0]['level']
    name = data[0]['name']
    for i in range(1, len(data)):
        level = data[i]['level']
        if level > max:
            max = level
            name = data[i]['name']
    return name, max


def filter_range(data, min, max):
    '''
    Takes a Pokemon list of dictionaries, a lower bound (inclusive) and upper bound (exclusive).
    Returns a list of Pokemon whose levels are within the bounds in the same order as the dataset.
    '''
    list = []
    for item in data:
        lvl = item['level']
        if lvl >= min and lvl < max:
            list.append(item['name'])
    return list


def mean_attack_for_type(data, type):
    '''
    Takes a Pokemon list of dictionaries and a Pokemon type string.
    Returns the average attack for all the Pokemon with the given type. 
    If no Pokemon of the type, returns None.
    '''
    sum = 0
    count = 0
    for item in data:
        if item['type'] == type:
            sum += item['atk']
            count += 1
    if count == 0:
        return None
    else:
        return sum / count


def count_types(data):
    '''
    Takes a Pokemon list of dictionaries 
    and returns a dictionary with the number of Pokemon for each type.
    '''
    types = {}
    for item in data:
        type = item['type']
        if type in types:
            types[type] += 1
        else:
            types[type] = 1
    return types


def mean_attack_per_type(data):
    '''
    Takes a Pokemon list of dictionaries and 
    returns a dictionary with the average attack of each type.
    '''
    types = {}
    for item in data:
        type = item['type']
        # 'type': [sum, count]
        if type in types:
            types[type][0] += item['atk']
            types[type][1] += 1
        else:
            types[type] = [item['atk'], 1]

    mean_vals = {}
    for key, value in types.items():
        mean_vals[key] = value[0] / value[1]
    print(mean_vals)
    return mean_vals
