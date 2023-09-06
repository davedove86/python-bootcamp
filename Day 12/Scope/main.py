################### Scope ####################

enemies = 1


def increase_enemies():
    # Modifying Global Scope - Do not do this, use a return statement as below
    global enemies
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()

print(f"enemies outside function: {enemies}")

# Use return statement to capture outside of scope rather than the global naming


def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1


enemies = increase_enemies()
print(f"enemies outside function: {enemies}")


################### Local Scope ####################

# Exists within functions - only valid within the function


def drink_potion():
    potion_strength = 2
    print(potion_strength)


drink_potion()
# print(potion_strength) - Will not print

################### Global Scope ####################
player_health = 10


def drink_potion():
    potion_strength = 2
    print(player_health)


drink_potion()

# There is no Block scope
# Anything insdide of an if, while etc is not scoped and can be accessed anywhere


################### Global Constants ####################
PI = 3.14159  # use uppercase for constants
URL = "https://www.google.com"
