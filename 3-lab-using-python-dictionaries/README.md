## Using Python Dictionaries

### Introduction

Dictionaries are one of the fundamental data types that we use in Python to solve real problems. These are handy when we don't need a sequential list of items, and it is more useful to have unique identifiers for looking up values. Being able to manipulate dictionaries and access items is necessary for effective programming. In this hands-on lab, we'll be working through some exercises demonstrating that we understand how to add, remove, modify, and read items from dictionaries in Python. We'll be asked to perform actions on a dictionary to meet some checkpoint requirements provided to us within a Python file.

To feel comfortable completing this lab you'll want to know how to do the following:

- Working with dictionary literals. Watch the "Dictionaries" video from the [Certified Entry-Level Python Programmer Certification course.
- Using Dictionary functions and methods. Watch the "Dictionary Methods" video from the Certified Entry-Level Python Programmer Certification course.



## The Scenario
From within the `using-dictionaries.py` file, we'll be modifying the `users` list so that the assertions throughout the file all succeed eventually. As we're working through the tasks we can run the file. Whenever Python gets to a line that starts with `assert`, it will raise an error and stop executing if we haven't met the criteria. The first error will look like this:

```bash
$ python3.7 using-dictionaries.py
Traceback (most recent call last):
  File "s9-lists/using-dictionaries-starter.py", line 3, in <module>
    assert users == [], f"Expected `users` to be [] but got: {repr(users)}"
NameError: name 'users' is not defined
```
This process will show us the line where the issue was encountered, and show us the differences between our expected and actual values.


**Problem**

```python
# 1) Set the emails variable to be an empty dictionary

assert emails == {}, f"Expected `emails` to be {{}} but got: {repr(emails)}"

# 2) Add 'ashley', 'craig', and 'elizabeth' to the emails dictionary without reassigning the variable.

assert emails == {
    "ashley": "ashley@example.com",
    "craig": "craig@example.com",
    "elizabeth": "elizabeth@example.com",
}, f"Expected `emails` to be {{'ashley': 'ashley@example.com', 'craig': 'craig@example.com', 'elizabeth': 'elizabeth@example.com'}} but got: {repr(emails)}"
# 3) Remove 'craig' from the emails dictionary without reassigning the variable.

assert emails == {
    "ashley": "ashley@example.com",
    "elizabeth": "elizabeth@example.com",
}, f"Expected `emails` to be {{'ashley': 'ashley@example.com', 'elizabeth': 'elizabeth@example.com'}} but got: {repr(emails)}"

# 4) Add 'dalton' to the emails dictionary without reassigning the variable.

assert emails == {
    "ashley": "ashley@example.com",
    "elizabeth": "elizabeth@example.com",
    "dalton": "dalton@example.com",
}, f"Expected `emails` to be {{'ashley': 'ashley@example.com', 'elizabeth': 'elizabeth@example.com', 'dalton': 'dalton@example.com'}} but got: {repr(emails)}"

# 5) Return a list of keys from the emails dictionary as `users`

assert users == [
    "ashley",
    "elizabeth",
    "dalton",
], f"Expected `users` to be ['ashley', 'elizabeth', 'dalton'] but got: {repr(users)}"

# 6) Return a list of values from the emails dictionary as `email_list`

assert email_list == [
    "ashley@example.com",
    "elizabeth@example.com",
    "dalton@example.com",
], f"Expected `email_list` to be ['ashely@example.com', 'elizabeth@example.com', 'dalton@example.com'] but got: {repr(email_list)}"

# 7) Return a list of tuples called `pairs` representing the key/value pairs in `emails`.

assert pairs == [
    ("ashley", "ashley@example.com"),
    ("elizabeth", "elizabeth@example.com"),
    ("dalton", "dalton@example.com"),
], f"Expected `pairs` to be [('ashley', 'ashley@example.com'), ('elizabeth', 'elizabeth@example.com'), ('dalton', 'dalton@example.com')] but got: {repr(pairs)}"

```


**Sollution**

```python
#!/usr/bin/env python3
# 1) Set the emails variable to be an empty dictionary
emails = {}
assert emails == {}, f"Expected `emails` to be {{}} but got: {repr(emails)}"

# 2) Add 'ashley', 'craig', and 'elizabeth' to the emails dictionary without reassigning the variable.
emails.update({
    "ashley": "ashley@example.com",
    "craig": "craig@example.com",
    "elizabeth": "elizabeth@example.com"
})
assert emails == {
    "ashley": "ashley@example.com",
    "craig": "craig@example.com",
    "elizabeth": "elizabeth@example.com",
}, f"Expected `emails` to be {{'ashley': 'ashley@example.com', 'craig': 'craig@example.com', 'elizabeth': 'elizabeth@example.com'}} but got: {repr(emails)}"

# 3) Remove 'craig' from the emails dictionary without reassigning the variable.
del emails['craig']
assert emails == {
    "ashley": "ashley@example.com",
    "elizabeth": "elizabeth@example.com",
}, f"Expected `emails` to be {{'ashley': 'ashley@example.com', 'elizabeth': 'elizabeth@example.com'}} but got: {repr(emails)}"

# 4) Add 'dalton' to the emails dictionary without reassigning the variable.
emails['dalton'] = 'dalton@example.com'
assert emails == {
    "ashley": "ashley@example.com",
    "elizabeth": "elizabeth@example.com",
    "dalton": "dalton@example.com",
}, f"Expected `emails` to be {{'ashley': 'ashley@example.com', 'elizabeth': 'elizabeth@example.com', 'dalton': 'dalton@example.com'}} but got: {repr(emails)}"

# 5) Return a list of keys from the emails dictionary as `users`
users = list(emails.keys())
assert users == [
    "ashley",
    "elizabeth",
    "dalton",
], f"Expected `users` to be ['ashley', 'elizabeth', 'dalton'] but got: {repr(users)}"

# 6) Return a list of values from the emails dictionary as `email_list`
email_list = list(emails.values())
assert email_list == [
    "ashley@example.com",
    "elizabeth@example.com",
    "dalton@example.com",
], f"Expected `email_list` to be ['ashely@example.com', 'elizabeth@example.com', 'dalton@example.com'] but got: {repr(email_list)}"

# 7) Return a list of tuples called `pairs` representing the key/value pairs in `emails`.
pairs = list(emails.items())
assert pairs == [
    ("ashley", "ashley@example.com"),
    ("elizabeth", "elizabeth@example.com"),
    ("dalton", "dalton@example.com"),
], f"Expected `pairs` to be [('ashley', 'ashley@example.com'), ('elizabeth', 'elizabeth@example.com'), ('dalton', 'dalton@example.com')] but got: {repr(pairs)}"
    
```