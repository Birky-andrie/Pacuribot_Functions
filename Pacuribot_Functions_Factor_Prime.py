# Function to find the smallest factor of a given number
def find_smallest_factor(n):
    if n < 2:
        print("Invalid input. Enter a number greater than 2.")
        return None

    # Iterate from 2 to the square root of n to find the smallest factor
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print(f"The smallest factor other than 1 for {n} is {i}.")
            return i

    # If no factor is found, the number is prime
    print(f"{n} is a prime number.")
    return n


# Function to find prime numbers within a given range
def find_prime_numbers_in_range(start, end):
    prime_numbers = []

    # Iterate through the range and check for prime numbers
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                prime_numbers.append(num)

    # Print the prime numbers found in the range
    if prime_numbers:
        print(f"Prime numbers in the range [{start}, {end}]: {prime_numbers}")
    else:
        print(f"No prime numbers found in the range [{start}, {end}].")


# Main loop
while True:
    try:
        # Prompt the user to select an option
        choice = int(input("Select an option \n 1: Find smallest factor \n "
                           "2: Find prime numbers in range \n 0: Exit):"))

        # Exit the loop if the user inputs 0
        if choice == 0:
            print("Exiting the program. Goodbye!")
            break

        # Based on the user's choice, execute the corresponding functionality
        if choice == 1:
            num = int(input("Enter an integer >= 2: "))
            find_smallest_factor(num)
        elif choice == 2:
            start_range = int(input("Enter the start of the range: "))
            end_range = int(input("Enter the end of the range: "))
            find_prime_numbers_in_range(start_range, end_range)
        else:
            print("Invalid choice. Please enter 1, 2, or 0.")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")
