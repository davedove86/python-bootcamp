# Data Types

# String
"Hello"
# Subscripting
print("Hello"[-1])

# Number

# Integer
print(123 + 456)

# Computer ignores _ if we write large numbers in the UK rather than adding a decimal
123_456_789

# Float
3.15

# Boolean
True
False

# Working with strings & numbers with type checking
num_char = len(input("What is your name? "))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters")

a = float(123)
print(type(a))

print(70 + float("100.5"))
print(str(70) + str(100))

# PEMDAS - Order of Priority when dealing with numbers
# Parentheses ()
# Exponents **
# Multiplication *
# Division /
# Addition +
# Subtraction -

# What will be printed
print(3 * 3 + 3 / 3 - 3)

# Change the priorty to get 3.0 - adding ()
print(3 * (3 + 3) / 3 - 3)
