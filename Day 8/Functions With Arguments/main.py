# Simple Function
def greet():
    print('Hello')
    print('Hello')
    print('Hello')


greet()

# Functions with Input


def greet_with_name(name):
    print(f'Hello {name}')
    print(f'Goodbye {name}')


greet_with_name('Dave')


# Functions with many Inputs
# Positonal Arguments
def greet_with_name(first_name, last_name):
    print(f'Hello {first_name} {last_name}')
    print(f'Goodbye {first_name}')


greet_with_name('Dave', 'Dove')

# Keyword Arguments


def greet_with_name(first_name, last_name):
    print(f'Hello {first_name} {last_name}')
    print(f'Goodbye {first_name}')


greet_with_name(first_name='Dave', last_name='Dove')
