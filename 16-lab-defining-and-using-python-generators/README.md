## Defining and Using Python Generators

Generators are Python functions that behave like iterators. By using generators, we're able to create sequences that are evaluated as each item is needed, making them more memory-efficient compared to simply having lists. In this hands-on lab, we'll be building a generator function that behaves like the built-in **range** function, except it will yield string characters instead of integers.

To feel comfortable completing this lab, you'll need to know how to do the following:

- Defining and using generators. Watch the "Defining and Using Generators" video from the Certified Entry-Level Python Programmer Certification course.

- Working with **for** loops. Watch the "The **for** Loop" video from the Certified Entry-Level Python Programmer Certification course.

- Using the **ord** and **chr** functions. Watch the "String Encodings and Functions" video from the Certified Entry-Level Python Programmer Certification course.



starting_code.py
```python
# Define the `char_range` generator here


# Tests to verify the implementation of char_range
# *Do not modify
##################################################

# Ensure that `char_range` is a generator function
from inspect import isgeneratorfunction

assert isgeneratorfunction(
    char_range
), f"Expected char_range to be a generator function but was not."

# Ensure that the result *does* includes the stop character
assert list(char_range("a", "e")) == [
    "a",
    "b",
    "c",
    "d",
    "e",
], f"Expected ['a', 'b', 'c', 'd', 'e'] but got {repr(list(char_range('a', 'e')))}"

# Iterate backwards if the start code point is higher than the stop code point

assert list(char_range("e", "a")) == [
    "e",
    "d",
    "c",
    "b",
    "a",
], f"Expected ['e', 'd', 'c', 'b', 'a'] but got {repr(list(char_range('e', 'a')))}"

# Properly step if a step value is provided

assert list(char_range("a", "e", 2)) == [
    "a",
    "c",
    "e",
], f"Expected ['a', 'c', 'e'] but got {repr(list(char_range('a', 'e', 2)))}"

# Step properly if the start code point is higher than the stop code point

assert list(char_range("e", "a", 2)) == [
    "e",
    "c",
    "a",
], f"Expected ['e', 'c', 'a'] but got {repr(list(char_range('e', 'a', 2)))}"
```
