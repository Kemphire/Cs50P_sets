'''Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due.
Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.'''

max_price = 50                                     # Setting initial due to 50 cause 50 is maximum price for coke
Due = max_price
total = 0                                    # Setting total total coin denomination to be 0.
inserted = int(input("Insert Coin: "))       # Asking user to insert coin.
total += inserted                            # Adding value of inserted coin to total value.
Due -= inserted                              # Updating due by subtracting it with previous value of coin inserted.


if inserted == 50 or inserted == 10 or inserted == 5:          # Checking if the inserted coin is of valid denomination or not. if it is then execute further.
    while total < max_price:                                          # Setting loop to execute whenever total is less than maximum accepted price i.e. 50.
        print("Amount Due:",Due)                               # Printing amount due means how much value of more coin to insert to reach the price i.e. 50.
        inserted = int(input("Insert Coin: "))                 # Once again ask for inserting coin if total is still less than 50.
        total += inserted                                      # Update total by adding previous value of coin inserted to already calculated total.
        Due -= inserted                                        # Updating due by subtracting the value of coin previously inserted.

        if total >= 50:                                        # If the total reaches to 50 or more.
            print("Change Owed:",(total - 50))                 # then print money that machine owe to user by subtracting total by 50.
            break                                              # break loop when total reaches to 50 or more.

elif inserted != 25 or inserted != 10 or inserted != 5:        # if inserted coin is not of valid denomination.
    Due = 50                                                   # Set Due to 50 for this case and don't update it for any invalid denomination.
    print("Amount Due:",Due)                                   # Print the Due to 50.




# One more apprach to solve this.

# Set the maximum price for a product
max_price = 50
Due = max_price  # Initialize the amount due with the maximum price

# Define valid coin denominations
valid = [25, 10, 5]
total = 0  # Initialize the total amount inserted by the user to 0

# Continue looping until the user has inserted enough coins to cover the price
while total < max_price:
    # Display the amount still due to reach the maximum price
    print(f"Amount Due: {Due}")

    # Ask the user to insert a coin and convert their input to an integer
    inserted = int(input("Insert Coin: "))

    # Check if the inserted coin is a valid denomination
    if inserted in valid:
        total += inserted  # Add the coin's value to the total
        Due -= inserted   # Subtract the coin's value from the amount due
    else:
        # If an invalid coin is inserted, display the current amount due
        print(f"Amount Due: {Due}")

# When the total reaches or exceeds the maximum price
if total >= max_price:
    # Calculate and display the change owed to the user
    print(f"Change Owed: {total - max_price}")






