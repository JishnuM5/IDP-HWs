[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/uypltgqh)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=16332577&assignment_repo_type=AssignmentRepo)
# HW3 - Pokémon

## Overview
**Learning objective:** Read, process, and group CSV data to compute descriptive statistics with and without Pandas.

You will want to read through the assignment thoroughly. Understand the context and methods you're implementing. There are _tips_ and _resources_ available to help you succeed - **take advantage of them!!**

- [Context](#context)
- [Your Assignment](#your-assignment)
  - [Without Pandas (Manual)](#without-pandas-manual)
  - [With Pandas (Library)](#with-pandas-library)
  - [Required Methods](#required-methods)
    - [species_count](#species_count)
    - [max_level](#max_level)
    - [filter_range](#filter_range)
    - [mean_attack_for_type](#mean_attack_for_type)
    - [count_types](#count_types)
    - [mean_attack_per_type](#mean_attack_per_type)
- [Files & Requirements](#files-and-tests)
  - [Provided Files](#provided-files)
  - [Submission Guidelines](#submission-guidelines)
  - [Rubric](#rubric)
- [Tips](#tips)
  - [Code Quality](#code-quality)
  - [Parsing](#parsing)
  - [Test Files](#test-files)
  - [Test Methods](#test-methods)
  - [Series to List](#series-to-list)
  - [Series to Dict](#series-to-dict)
- [Other Resources](#other-resources)
- [Challenge Question (OPTIONAL)](#challenge-question)
  - [Tips for Challenge Question](#tips-for-challenge-question)

## Context
In the [Pokémon](https://en.wikipedia.org/wiki/Pok%C3%A9mon) video game series, the player catches pokemon, fictional creatures trained to battle each other as part of a sport franchise. Pokémon exerted significant cultural influence on people who grew up in the late 1990s and early 2000s not only in its country of origin, Japan, but also around the world. More recently, [Pokémon Go](https://en.wikipedia.org/wiki/Pok%C3%A9mon_Go) became a viral hit as hundreds of millions of people played the augmented-reality game at its peak during the summer of 2016. You do not need to understand the details of Pokémon or need to have played the game to do the assignment. All you need to understand is the statistics we provide in our dataset about each pokemon.

The `pokemon_box.csv` file stores some imagined data about a player’s pokemon in the following format:

| id  | name       | level | personality | type  | weakness | atk | def | hp  | stage |
|-----|------------|-------|-------------|-------|----------|-----|-----|-----|-------|
| 1   | Bulbasaur  | 12    | Jolly       | Grass | Fire     | 45  | 50  | 112 | 1     |

- `id` is a unique numeric identifier corresponding to the species of a pokemon. All pokemon of the same species share the same id.
- `name` is the name of the species of pokemon, such as Bulbasaur.
- `level` is the integer level of the pokemon.
- `personality` is a one-word string describing the personality of the pokemon, such as Jolly.
- `type` is a one-word string describing the type of the pokemon, such as Grass.
- `weakness` is the enemy type that this pokemon is weak toward. Bulbasaur is weak to fire-type pokemon.
- `atk`, `def`, and `hp` are integers that indicate the attack power, defense power, and hit points of the pokemon.
- `stage` is an integer that indicates the particular developmental stage of the pokemon.

In the Charmander species, Charmander begins at stage 1, evolves into a Charmeleon at stage 2, and finally evolves into Charizard at stage 3.

![Charmander stages](https://courses.cs.washington.edu/courses/cse163/22sp/assets/images/pokemon.png)

The problems in this assessment focus on providing [descriptive statistics](https://en.wikipedia.org/wiki/Descriptive_statistics) for summarizing the pokemon dataset, such as computing the mean or count of a certain column. Solve each problem in two ways.

## Your Assignment 
### Without Pandas (Manual)
Use Python built-in data structures plus Python math functions to solve the problems in the file `hw3_manual.py`. These 6 functions take a list of dictionaries representing the parsed pokemon dataset.

```python
data = parse('pokemon_box.csv')

print('Number of species:', hw3_manual.species_count(data))
print('Highest level pokemon:', hw3_manual.max_level(data))
print('Low-level Pokemon:', hw3_manual.filter_range(data, 1, 9))
print('Average attack for fire types:', hw3_manual.mean_attack_for_type(data, 'fire'))
print('Count of each Pokemon type:')
print(hw3_manual.count_types(data))
print('Average attack for each Pokemon type:')
print(hw3_manual.mean_attack_per_type(data))
```

### With Pandas (Library)
Use Pandas (plus Python math functions) in `hw3_pandas.py`. **Do not use any loops or list/dictionary comprehensions.** These 6 functions take a Pandas DataFrame representing the parsed pokemon dataset.

```python
data = pd.read_csv('pokemon_box.csv')

print('Number of species:', hw3_pandas.species_count(data))
print('Highest level pokemon:', hw3_pandas.max_level(data))
print('Low-level Pokemon:',  hw3_pandas.filter_range(data, 1, 9))
print('Average attack for fire types:', hw3_pandas.mean_attack_for_type(data, 'fire'))
print('Count of each Pokemon type:')
print(hw3_pandas.count_types(data))
print('Average attack for each Pokemon type:')
print(hw3_pandas.mean_attack_per_type(data))
```
#### You may assume the following:

The data is never empty (there’s at least one pokemon) and that there’s no missing data (each pokemon has every attribute).

#### You may NOT assume the following:

Canonically, Pokémon cannot have an attack stat of 0. For this assessment, however, you should NOT make that assumption.

### Required Methods
There are six methods to implement: [`species_count`](#species_count), [`max_level`](#max_level), [`filter_range`](#filter_range), [`mean_attack_for_type`](#mean_attack_for_type), [`count_types`](#count_types), and [`mean_attack_per_type`](#mean_attack_per_type). 

For each method described in the tabs you must: 

* <i class="fas fa-pen-square fa-fw"></i> **Write** in `hw3_manuals.py` the function as described in the tabs.  
* <i class="fas fa-pen-square fa-fw"></i> **Write** in `hw3_pandas.py` the same function using Pandas. Rather than take a list of dictionaries, the Pandas version will take a `DataFrame` argument.   
* <i class="fas fa-pen-square fa-fw"></i> **Write** in `hw3_test.py` one or more test functions that call the method with various input. Compare the actual results to the expected results using `assert_equals`. Do **not** do all your testing with the `pokemon_test.csv` file; be sure to add 2 (**two**) additional test cases by creating your own CSV files. (See the [Tips](#tips) section). You must test **ALL** methods - both manual and pandas.


Don't forget that for _each_ method, you will have _two_ solutions - one in `hw3_manual.py` and one in `hw3_pandas.py`. **The results from the two implementations should be identical.** The difference is that the manual methods accept a _list of dictionaries_ while the Pandas methods accept a _DataFrame_. There are proper ways to reduce redundancy.

There is an optional [Challenge Question](#challenge-question) available. It is optional and not graded; **there is no extra credit available for completing it. It is purely for those who are curious and want to experiment.**

#### species_count
<i class="fas fa-pen-square fa-fw"></i> Write a function `species_count` that takes a parsed pokemon dataset and returns the number of unique pokemon species in the dataset as determined by the `name` attribute without using Pandas.

For the `pokemon_test.csv` file, `species_count(data)` should return `3`.

**Important:** Do not use the `id` attribute to solve this problem, you **MUST** use the `name` attribute. It doesn't make sense, but this follows the ideas that the UW assignment provides, so go with it and use `name`.

#### max_level
<i class="fas fa-pen-square fa-fw"></i> Write a function `max_level` that takes a parsed pokemon dataset and returns a 2-element tuple of the `(name, level)` of the pokemon with the highest `level` in the dataset. If there is more than one pokemon with the highest `level`, return the pokemon that appears first in the file.

For the `pokemon_test.csv` file, `max_level(data)` should return the 2-element tuple, `('Lapras', 72)`.

#### filter_range
<i class="fas fa-pen-square fa-fw"></i> Write a function `filter_range` that takes a parsed pokemon dataset and  two numbers: a lower bound (inclusive) and upper bound (exclusive). The function returns a list of the names of pokemon whose `level` fall within the bounds in the same order that they appear in the dataset.

For the `pokemon_test.csv` file, `filter_range(data, 35, 72)` should return `['Arcanine', 'Arcanine', 'Starmie']`. Note that Lapras is not included because the upper bound is exclusive of Lapras, which is exactly level 72.

Note: To convert a Series to a list, look [here](#series-to-list) for help.

#### mean_attack_for_type
<i class="fas fa-pen-square fa-fw"></i> Write a function `mean_attack_for_type` that takes a parsed pokemon dataset and a string representing the pokemon `type`. The function returns the average `atk` for all the pokemon in the dataset with the given `type`. If there are no pokemon of the given `type`, return `None`.

For the `pokemon_test.csv` file, `mean_attack_for_type(data, 'fire')` should return `47.5`.

#### count_types
<i class="fas fa-pen-square fa-fw"></i> Write a function `count_types` that takes a parsed pokemon dataset and returns a dictionary representing for each pokemon `type` the number of pokemon of that `type`. The order of the keys in the returned dictionary does not matter.

For the `pokemon_test.csv` file, `count_types(data)` should return `{'fire': 2, 'water': 2}`.

Note: To convert a Series to a dictionary, look [here](#series-to-dict) for help.

#### mean_attack_per_type
<i class="fas fa-pen-square fa-fw"></i> Write a function `mean_attack_per_type` that takes a parsed pokemon dataset and returns a dictionary representing for each pokemon `type` the average `atk` of pokemon of that `type`. The order of the keys in the returned dictionary does not matter.

For the `pokemon_test.csv` file, `mean_attack_per_type(data)` should return `{'fire': 47.5, 'water': 140.5}`.


## Files and Tests

### Provided Files
**Note:** This list of files has some _non-runnable_ files which do not use the _main-method_ pattern. The methods inside them are run, but we do not run the file directly using the Run button in VS Code.

- `hw3_manual.py` is the _non-runnable_ file for you to put your implementations for solving each problem without Pandas. 
- `hw3_pandas.py` is the _non-runnable_ file for you to put your implementations for solving each problem with Pandas.
- `hw3_test.py` is the file for you to put your own tests. Be sure to use the _main-pattern_ for this file. Make sure it runs successfully!
- `cse163_utils.py` is a helper file that has code to help you test your code.
  - Contains the method `parse`, takes a filepath to a CSV and returns a list of dictionaries (use for `hw3_manual.py` testing)
  - Contains the method `assert_equals`, takes two objects and compares their contents to be the same (use in `hw3_test.py` to compare expected values and the results of your implementation)
- `pokemon_box.csv` is a large CSV file that stores information about pokemon. Do not modify it.
- `pokemon_test.csv` is a very small CSV file that stores information about pokemon used for the example cases. You may use this in your own personal tests, but do not modify.

### Submission Guidelines
You must submit your work as your teacher requires. Ask questions in class.

The following Python files must be present in your repository:

- `hw3_test.py`
- `hw3_pandas.py`
- `hw3_manual.py`

Any additional test files (like CSVs) used in your test methods should be contained in a subdirectory called test. A sample relative file path, from your root directory, may look like:

- `test/<test_file>.csv`

Do **NOT** modify the following files:

- `.vscode/settings.json`
- `pokemon_test.csv`
- `pokemon_box.csv`

### Rubric

# Python Assignment Grading Rubric

| Category | A (Excellent) | B (Satisfactory) | C (Needs Improvement) | F (Unsatisfactory) |
|----------|---------------|------------------|------------------------|---------------------|
| Behavior | Pass all teacher tests for all functions | Pass the common cases for all functions | Not passing the common cases for any of the functions | No modifications to the original template |
| Language/Library | Efficient and non-redundant solution for mean_attack_per_type; No other redundancies or inefficient solutions | All variables declared in local scope; "Heavy-weight" values stored in constants; Proper use of casting when possible; Minor redundancies allowed | Not using main method pattern in test file; Improper use of global variables; Inefficient data manipulation; Unnecessary looping in pandas solutions | No modifications to the original template |
| Style/Documentation | All required descriptions in function comments; Descriptive file header comments | Passes flake8 in both files; All functions commented; Complete file header comments; Reasonable function descriptions; Correct naming conventions | Not passing flake8 in either file; Missing or misplaced function comments; Missing file header comments; Incorrect naming conventions | Code extremely difficult to read and impossible to follow |
| Testing | All required tests present (1 spec test and 1 additional test per function); Efficient dataset parsing | No errors/warnings when running tests; Properly split tests; All test functions called from main | Test cases produce errors/warnings; Missing test functions; Improper test splitting; Not using assert_equals | No modifications to the original template |

Note: 

- For Language/Library, some minor redundancies are allowed for a B grade, particularly in the mean_attack_per_type function.
- For Style/Documentation, an A grade requires more detailed and accurate comments compared to a B grade.
- For Testing, an A grade emphasizes efficiency in dataset parsing, while a B grade focuses on basic correctness and structure.

## Tips
### Code Quality
Assessment submissions should pass these checks: `flake8`, and <a href="https://courses.cs.washington.edu/courses/cse163/22sp/resources/code_quality/" target="_blank">code quality guidelines</a>. The code quality guidelines are very thorough. For this assessment, the most relevant rules can be found in these sections, with the **bolded** one being new from the last homework:  

* <a href="https://courses.cs.washington.edu/courses/cse163/22sp/resources/code_quality/#naming-conventions" target="_blank">Naming</a>  
* <a href="https://courses.cs.washington.edu/courses/cse163/22sp/resources/code_quality/#documentation" target="_blank">Documentation</a>   
* <a href="https://courses.cs.washington.edu/courses/cse163/22sp/resources/code_quality/#efficiency-and-redundancy" target="_blank">Efficiency and Redundancy</a>  
    * Boolean Zen  
    * Loop Zen  
    * Factoring   
    * Unnecessary Cases
    * **No Looping with Pandas in `hw3_pandas.py`**
* Provide descriptive comments for each method using **docstring** comments
* Do **NOT** use globals in your test file. Instead, use constants or method parameters.   
* Don't make "heavy weight" constants. (See: <a href="https://courses.cs.washington.edu/courses/cse163/22sp/resources/code_quality/#constant-names" target="_blank">Code Quality - Constants</a> for more details.)  
* Attempt to keep declarations and values in close proximity to where they are used. This helps the reader understand the code better. This means, define expected values in the method where they are used.  
* Attempt to reduce redundancy with code instead of copy/paste. But, in test files, some redundancy is allowed so that tests can remain insulated from one another and to improve readability of individual test functions.   

### Parsing
Here you can see examples of both parsing functions:  
* `parse`: To help test functions solved without Pandas, `cse163_utils.py` defines a `parse` function that takes a filename and returns the dataset as a list of dictionaries.   
* `read_csv`: To help test functions solved with Pandas, call `pd.read_csv` to return the dataset as a `DataFrame`.  
```python
from cse163_utils import parse
import pandas as pd

df = pd.read_csv('file.csv')
list_of_dict = parse('file.csv')
```
### Test Files
* **Organize** and **create** additional CSV files for testing. Put them in a `test/` subdirectory.
* When specifying file names, use **relative** paths, such as `pd.read_csv('pokemon_test.csv')`.  
* **Do not** use the `pokemon_box.csv` file in your own test cases. The file is too large to come up with the correct answer on your own; it is  **not valid** to assume your code's output is the correct answer and to blindly use that as the expected value. It defeats the purpose of testing!

### Test Methods
* Write at least one test function for each problem and give it a descriptive name that indicates the function being tested, such as `test_species_count`.  
* In addition to the provided `pokemon_test.csv` example file, add at least 2 (**two**) additional test files (one file for each case you're testing). These data files contain short, contrived, targeted data that is easy to verify in your tests.  
* One test function per problem is fine since both ways of solving the problem should compute the same result. In other words, you may choose to write one method, `test_species_count` that tests both the manual and pandas code.  


### Series to List
To convert a Pandas Series to a list, use the built-in list function. For example:  
```python
# data is a DataFrame storing following info:
# name,age,species
# Fido,4,dog
# Meowrty,6,cat
# Chester,1,dog
# Phil,1,axolotl
names = data['name']  # Series
list(names)  # ['Fido', 'Meowrty', 'Chester', 'Phil']
row = data.loc[1]  # Series
list(row)  # ['Meowrty', 6, 'cat']
```
### Series to Dict
To convert a Pandas Series to a dictionary, use the built-in `dict` function. The dictionary keys are determined by the series index. For example:  
```python
# data is a DataFrame storing following info:
# name,age,species
# Fido,4,dog
# Meowrty,6,cat
# Chester,1,dog
# Phil,1,axolotl
names = data['name']  # Series
dict(names)  # {0: 'Fido', 1: 'Meowrty', 2: 'Chester', 3: 'Phil'}
row = data.loc[1]  # Series
dict(row)  # {'name': 'Meowrty', 'age': 6, 'species': 'cat'}
```

## Other Resources
These resources are organized in the [`resources/`](resources/README.md) subdirectory. These will be available to you for every homework assignment. **Make use of them - they contain valuable information!**

Useful files in this folder for this homework assignment include, but are not limited to:
- [collections.md](resources/api/collections.md)
- [pandas_api.md](resources//api/pandas_api.md)
- [writing_comments.md](resources/misc/writing_comments.md)
- [flake8.md](resources/misc/lake8.md)

## Challenge Question

**NOTE**: If you implement this challenge question, you'll need to document all methods fully with doc-strings so that all the grading scripts pass. You don't want to have your grade drop!  Be sure to test it, too!  

<i class="fas fa-pen-square fa-fw"></i> **Write** a class named `MyStats` inside the file `hw3_manual.py`. It will implement
several methods to support the required functionality. The `class` will have a static method named `compute` that will calculate three
statistics using Python libraries; do not implement the calculations yourself.  

Here are the three relatively esoteric statistics that the `compute` method provides:  
1) **Kurtosis**: Kurtosis is a measure of the tailedness or shape of a probability distribution. It quantifies whether the distribution has heavy tails or is more peaked compared to a normal distribution. You can calculate the kurtosis using the `scipy.stats.kurtosis` function.   
2) **Skewness**: Skewness measures the asymmetry of a probability distribution. It indicates whether the distribution has a longer tail on one side compared to the other. Positive skewness means the tail is on the right side, while negative skewness means the tail is on the left side. You can calculate the skewness of a distribution using the `scipy.stats.skew` method.  
3) **95th Percentile**: Numpy provides a convenient way to calculate percentiles. A percentile represents the values below which a given percentage of the data falls. For example, the 50th percentile is the median. Numpy's percentile function allows you to calculate percentiles easily for a given list of numbers. You will calculate the 95th percentile.

Here is sample code that shows how client code can use the class:  
```python
'''
This file is named: my_client.py
'''
# import the MyStats class from the file that implements it
from hw3_manual import MyStats

# Sample list on which to calculate three stats
l = [1, 2, 3, 4, 5, 6, 7, 10, 15]

# unpack the three statistics directly from the method call
a, b, c = MyStats.compute(l)

# store the results object (which is of type MyStats) from the method call
obj = MyStats.compute(l)

# print the object directly
print(obj) # prints: MyStats(kertosis=0.10, skew=0.98, 95_percentile=13.00)

# print the three unpacked statistics (raw & unrounded)
print(a, b, c)

# iterate the object and print each stat rounded to 3 decimal places
for s in obj:
    print(f'Stat = {s:.3f}')
```
The expected output of the above code is:  
```
MyStats(kertosis=0.10, skew=0.98, 95_percentile=13.00)
0.10378287249864737 0.9838565052198887 12.999999999999998
Stat = 0.104
Stat = 0.984
Stat = 13.000
```
Several higher Object Oriented pieces of functionality are present. You need to figure them out.  

### Tips for Challenge Question
* Use an <a href="https://docs.python.org/3/library/functions.html#staticmethod" target="_blank">annotation</a> to designate `compute` to be a static method.  
* Use <a href="https://docs.python.org/3/reference/datamodel.html#special-method-names" target="_blank">special methods</a> to allow the object to be _iterable_ and _printable_.  
* Consider leveraging a list's inherent ability to be _iterable_ to simplify the object's required implementation.  
* Follow privacy rules by using Python's naming conventions (using underscores) for private instance field names.   
