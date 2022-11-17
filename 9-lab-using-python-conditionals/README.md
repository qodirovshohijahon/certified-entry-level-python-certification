## Using Python Conditionals

### ABOUT THIS LAB

The majority of programs that we write will need to be more than a single sequential path of execution. We usually work with data that isn't always the same, and occasionally requires us to do different things based on that data. To achieve this we need to utilize conditionals. In this hands-on lab, we'll work through the conditional logic for the popular interviewing Fizz-Buzz problem by creating a script that will prompt the user for a number and then print out either the number, `"Fizz"`, `"Buzz"`, or `"FizzBuzz"` depending on whether the number meets one of the `Fizz-Buzz` requirements.

To feel comfortable completing this lab you'll want to know how to do the following:

- Utilize conditionals. Watch the "The `if` and `else` Statements" and "Handling Multiple Cases with elif" videos from the Certified Entry-Level Python Programmer Certification course.
- Handle user `input`. Watch the "The input Function" video from the Certified Entry-Level Python Programmer Certification course.



**Solution**

```python
value = int(input("Enter an integer value: "))

if value % 3 == 0 and value % 5 == 0 :
    print("FizzBuzz")
elif value % 5 == 0:
    print("Buzz")
elif value % 3 == 0:
    print("Fizz")
else:
    print(value)   
```