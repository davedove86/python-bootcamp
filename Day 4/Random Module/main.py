import random
import my_module

random_int = random.randint(1, 10)
print(f'Your randmon number is {random_int}')

# 0.0000000 - 0.9999999...
random_float = random.random() * 5
print(random_float)


print(f'PI = {my_module.pi}')
