# Generators
For HW6, SpellChecker, you need to learn about `generators`.   

In Python, a generator is a special type of function that produces a sequence 
of values, one at a time, when iterated over. Generators are different from 
regular functions in that they do not return all their output at once; instead, 
they `yield` their values one at a time, which allows them to be more memory-efficient 
than regular functions that return all their output at once.  

Here is a simple example of a generator in Python:

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for i in countdown(5):
    print(i)
```
This generator, countdown, yields the values 5, 4, 3, 2, and 1, one at a time, 
when it is iterated over. When the generator is called, it does not execute the 
code inside of it immediately; instead, it returns a special type of iterator 
called a "generator iterator", which can be used to execute the code in the 
generator one step at a time.

Generators can be very useful for producing large sequences of data, because 
they allow you to generate the values one at a time, rather than creating a 
list with all the values at once, which can be very memory-intensive.

Here are a couple of YouTube videos that explain generators in Python:

* [Python Generators: (By Socratica)](https://www.youtube.com/watch?v=gMompY5MyPg)  
* [Python Generators Explained (With Examples) (By Corey Schafer)](https://www.youtube.com/watch?v=bD05uGo_sVI)

These videos provide a good overview of generators, including how to create them, 
how to use them, and some of the benefits of using generators in your Python code.