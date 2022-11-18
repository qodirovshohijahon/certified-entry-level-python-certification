### **Basic Concepts**

**3. What would be the output of the following code?**

```python
ages = {'Keith': 30, 'Levi': 25, 'John': 20}
age = ages.get('Kevin')
print(age)
```

**:x:** 30
- There is no Kevin key, so we would not print 30.

- Video for reference: Dictionary Methods


**:white_check_mark: None**
- The get method returns None since the Kevin key is not present in the dictionary.

- Video for reference: Dictionary Methods


------------------

**18. What built-in function is used to write characters to the terminal?**

**:white_check_mark: The print function**

- The print function is the primary way that we write to the terminal.

- Video for reference: The print Function

**:x: The input function**

- The input function can write to the terminal, but it is primarily used to read in user input.

- Video for reference: The print Function

--------------


### **Data Types, Evaluations, and Basic I/O Operations**


**9. What would be the output of this code?**
```python
val = 1 or '2'
val *= 3
print(val)

```
**:white_check_mark: 3**

- The initial value of val is `1`, so after it is multiplied by `3` and reassigned using `=`, the printed result is `3`.

- Video for reference: Boolean Operators


**:x:'6'**

- String multiplication wouldn't ever lead to a '6' being returned.

- Video for reference: Boolean Operators


**14. What is the value of num2 after executing this code?**
```python
num = 12
num2 = num
num = num + 1
num2 = num2 / 2
```
**:x: 6**
- Standard division always returns a float, so it won't be an integer.

- Video for reference: Variables and Assignment Operator

**:white_check_mark: 6**

- After the initial assignment of `num2 = num`, we no longer need to be concerned with the value of `num`. So, the final value will be the result of `12 / 2`.

- Video for reference: Variables and Assignment Operator



### **Flow Control**

**28. What is the output of this code?**
```python
for num in range(1, 10, 2):
    if num % 3:
        print(num)
```

**:x: 3 9**

- The values 3 and 9 would cause the condition to return 0 which is a False value, so these two values wouldn't be printed.

- Video for reference: The for Loop

**:white_check_mark: Nothing will be printed.**

- 1 5 7
- Only `1`, `5`, and `7` from the stepped range (1,3,5,7,9) would cause the condition to return a non-zero value. Since zero is a `False` value, the other numbers (3,9) will not be printed.

- Video for reference: The for Loop

### **Data Collections**

**15. What code would result in the expected output when inserted into the commented line?**

Expected Output:

`False`

Code:
```python 
values = ['Kevin Bacon', 60, '555-555-5555', False]
# Code goes here
print(val)
```

**:x: `val = '555-555-5555' is not in values`**
- There is no is not in operator so this would cause an error.

- Video for reference: Lists

**:white_check_mark: val = not values[1]**
- This would set val to False.

- Video for reference: Lists


**11. What would be the value of names after running this code?**

```python
names = ['Alice', 'Bob', 'Lance', 'Mike']
names = names[::-1]
```

`:white_check_mark: ['Mike', 'Lance', 'Bob', 'Alice']`
- The slice of `[::-1]` reverses the list and since we're reassigning to the `names` variable it changes the values of `names`.

- Video for reference: Lists

`:x: ['Mike']`

- We're not returning a slice that only consists of the last value in the original list.

- Video for reference: Lists


**1. What would be the value of all_names after running this code?**
```python
names = ['Alice', 'Bob', 'Lance', 'Mike']
all_names = names
names.remove('Bob')
all_names + ['Kevin']
```


`:white_check_mark: ['Alice', 'Lance', 'Mike']`
- Because lists are mutable and `all_names` and `names` point to the same mutable list, making changes to one will also change the other.

- Video for reference: Lists


`:x: ['Alice', 'Lance', 'Mike', 'Kevin']`
- The addition operator does not change the initial list, so 'Kevin' would not be in the list.

- Video for reference: Lists

--------------


### **Functions**

**25. What would be the output of the following code?**
```python
def add_five(num1, num2=5):
    num1 + num2
print(add_five(1, 2))
```

**:x: 3**
- Because the add_five function doesn't have a return statement, it will always evaluate to None.

- Video for reference: Defining and Using Functions


**:white_check_mark: None**
- Because the add_five function doesn't have a return statement, it will always evaluate to None.

- Video for reference: Defining and Using Functions


**16. What would be the output of the following code?**

```python
def fizz(num):
    if num % 3 == 0 and num % 5 == 0:
      return 'FizzBuzz'
    elif num % 3 == 0:
      return 'Fizz'
    elif num % 5 == 0:
      return 'Buzz'
    else:
      return num

fizz(14)
```

**:x: 14**
- The number 14 will be returned from the function, but print function is not used, so there is no output.

- Video for reference: Defining and Using Functions

**:white_check_mark: There is no output printed.**

- Because the fizz function returns a value instead of calling print this code will not output anything.

- Video for reference: Defining and Using Functions