# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25

# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

# Write your code below this line 👇
bill = 0

if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
else:
    bill += 25

if add_pepperoni == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3

if extra_cheese == 'Y':
    bill += 1

print(f'Your final bill is: ${bill}.')


# total = 0
# small_pizza = 15
# medium_pizza = 20
# large_pizza = 25

# if size == 'S':
#     total = small_pizza
#     if add_pepperoni == 'Y':
#         total += 2
#     if extra_cheese == 'Y':
#         total += 1

# if size == 'M':
#     total = medium_pizza
#     if add_pepperoni == 'Y':
#         total += 3
#     if extra_cheese == 'Y':
#         total += 1

# if size == 'L':
#     total = large_pizza
#     if add_pepperoni == 'Y':
#         total += 3
#     if extra_cheese == 'Y':
#         total += 1

# print(f'Your final bill is: ${total}.')
