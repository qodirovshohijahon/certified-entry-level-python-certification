### **Basic Concepts**

**3. What would be the output of the following code?**

```python
ages = {'Keith': 30, 'Levi': 25, 'John': 20}
age = ages.get('Kevin')
print(age)
```

**x** 30
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

**x The input function**

The input function can write to the terminal, but it is primarily used to read in user input.

Video for reference: The print Function

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


**x'6'**

- String multiplication wouldn't ever lead to a '6' being returned.

- Video for reference: Boolean Operators


**14. What is the value of num2 after executing this code?**
```python
num = 12
num2 = num
num = num + 1
num2 = num2 / 2
```
**x 6**
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

**x 3 9**

- The values 3 and 9 would cause the condition to return 0 which is a False value, so these two values wouldn't be printed.

- Video for reference: The for Loop

**:white_check_mark: Nothing will be printed.**

- 1 5 7
- Only `1`, `5`, and `7` from the stepped range (1,3,5,7,9) would cause the condition to return a non-zero value. Since zero is a `False` value, the other numbers (3,9) will not be printed.

- Video for reference: The for Loop