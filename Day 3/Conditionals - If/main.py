print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

# If Statement
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input('What is your age? '))
    # nested If statement
    if age <= 12:
        bill = 3
        print('Child tickets are £3')
    elif age <= 18:
        bill = 5
        print('Youth tickets are £5')
    elif age >= 45 and age <= 55:
        print('Everything is going to be ok. Have a free ride on us!')
    else:
        bill = 7
        print('Adults tickets are £7')

    wants_photo = input("Do you want a photo taken> Y or N ")
    if wants_photo == 'Y':
        bill += 3

    print(f'Your final bill is £{bill}')


else:
    print("Sorry, you cannot ride this rollercoaster")
