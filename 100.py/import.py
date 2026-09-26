if (1 == 01):
    print("Yes")
else:
    print("No")
'''it gives an error bcz in python when we write the 0 it actuually
in Python 3.x, using a leading zero for a non-binary, non-octal, or non-hexadecimal literal
is no longer allowed, so 01 will raise a SyntaxError. In Python 3.x, octal numbers must be 
written with a 0o prefix, like 0o1.
In Python, integers can be represented in different bases: binary, octal, decimal, and hexadecimal. Here's how each is represented:

### 1. **Binary (Base-2)**
   - Prefix: `0b` or `0B`
   - Digits: `0` and `1`
   - Example:
     ```python
     binary_number = 0b1010  # 10 in decimal
     print(binary_number)  # Output: 10
     ```

### 2. **Octal (Base-8)**
   - Prefix: `0o` or `0O`
   - Digits: `0` to `7`
   - Example:
     ```python
     octal_number = 0o12  # 10 in decimal
     print(octal_number)  # Output: 10
     ```

### 3. **Decimal (Base-10)**
   - This is the standard number system and requires no prefix.
   - Digits: `0` to `9`
   - Example:
     ```python
     decimal_number = 10
     print(decimal_number)  # Output: 10
     ```

### 4. **Hexadecimal (Base-16)**
   - Prefix: `0x` or `0X`
   - Digits: `0` to `9` and `a` to `f` (or `A` to `F` for uppercase)
   - Example:
     ```python
     hexadecimal_number = 0xA  # 10 in decimal
     print(hexadecimal_number)  # Output: 10
     ```

### Summary of Number Representations:
- **Binary**: `0b1010` (10 in decimal)
- **Octal**: `0o12` (10 in decimal)
- **Decimal**: `10`
- **Hexadecimal**: `0xA` (10 in decimal)

These prefixes allow Python to interpret the number in the correct base.




'''
