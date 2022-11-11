**str**ings are the primary way that we interact with non-numerical data in programming, and the str type in Python provides us with a lot of powerful methods to make working with string data easier. In this hands-on lab, we'll be creating a script that can take a user-provided message and perform various actions on it before printing out those new results.

To feel comfortable completing this lab you'll want to know how to do the following:

- Utilize methods on the **str** class. Watch the "Using String Methods" from the Certified Entry-Level Python Programmer Certification course.
- Working with list literals. Watch the "Lists" video from the Certified Entry-Level Python Programmer Certification course.
Using List functions and methods. Watch the "List Functions and Methods" video from the Certified Entry-Level Python Programmer Certification course.


**LEARNING OBJECTIVES**

- Create the variations.py Script, Make It Executable with python3.7, and Accept User Input

- Print the Lowercase, Uppercase, Title Case, and Capitalized Versions of the User's Input

- Separate the String and Present the Individual Words as a List

- Print the Alphabetic First and Last Words from the User's Input



## Using Python String Methods

### Introduction

Strings are the primary way that we interact with non-numerical data in programming, and the **str** type in Python provides us with a lot of powerful methods to make working with string data easier. In this hands-on lab, we'll be creating a script that can take a user-provided message and perform various actions on it before printing out those new results.

To feel comfortable completing this lab you'll want to know how to do the following:

- Utilize methods on the str class. Watch the "Using String Methods" from the Certified Entry-Level Python Programmer Certification course.

- Working with list literals. Watch the "Lists" video from the Certified Entry-Level Python Programmer Certification course.

- Using List functions and methods. Watch the "List Functions and Methods" video from the Certified Entry-Level Python Programmer Certification course.

**The Scenario**

Our script `variations.py` will allow us to provide a string and then it will present us with some permutations (all lowercase, all uppercase, etc.), of that string. The script will also tell us the string's first and last words, when they are sorted alphabetically. We'll need to utilize numerous methods on the **str** class and some of the functions used to sort lists to make all of this this happen. Here's how we want the script to be used:


**Additional Resources**

Our script `variations.py` will allow us to provide a string and then it will present us with some permutations (all lowercase, all uppercase, etc), of that string. The script will also tell us the string's first and last words, when they are sorted alphabetically. We'll need to utilize numerous methods on the **str** class and some of the functions used to sort lists to make all of this this happen. Here's how we want the script to be used:

```yaml
$ ./variations.py
Enter a message: This is my message
Lowercase: this is my message
Uppercase: THIS IS MY MESSAGE
Capitalized: This is my message
Title Case: This Is My Message
Words: ['This', 'is', 'my', 'message']
Alphabetic First Word: is
Alphabetic Last Word: This
```


**Sollution**

```python
#!/usr/bin/env python3

message = input("Enter a message: ")
print(f"Lowercase: {message.lower()}")
print(f"Uppercase: {message.upper()}")
print(f"Capitalized: {message.capitalize()}")
print(f"Title Case: {message.title()}")
# splitted_message = str(message).split()
# print("Words: " + splitted_message)
# alph_first_word = message.split()
# print(f"Alphabetic First Word: {splitted_message}")
print(f"Alphabetic Last Word: {message.capitalize()}")

words = [word for word in message.split()]
sorted_words = words.sort()
print(sorted_words)
```

Lowercase: this is my message
Uppercase: THIS IS MY MESSAGE
Capitalized: This is my message
Title Case: This Is My Message

Enter a message: This is a test Message!
Lowercase: this is a test message!
Uppercase: THIS IS A TEST MESSAGE!
Capitalized: This is a test message!
Title Case: This Is A Test Message!
Words: ['This', 'is', 'a','test','Message!']