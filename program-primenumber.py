# Simple Python program to check if a number is prime

print("--- Prime Number Checker ---")

while True:
    try:
        # 1. Get input from the user
        num_str = input("\nEnter a whole number to check (or 'q' to quit): ")

        # Allow user to quit
        if num_str.lower() == 'q':
            print("Exiting Prime Number Checker. Goodbye!")
            break # Exit the while loop

        num = int(num_str) # Convert input string to an integer

        # 2. Check for basic conditions
        if num <= 1:
            # Numbers less than or equal to 1 are not prime
            print(f"{num} is NOT a prime number (prime numbers must be > 1).")
        elif num == 2:
            # 2 is the only even prime number
            print(f"{num} IS a prime number.")
        else:
            # Assume it's prime until proven otherwise
            is_prime = True
            # 3. Loop from 2 up to half of the number
            # We only need to check divisors up to num // 2.
            # If a number has a divisor greater than its half, it must also have one smaller than its half.
            # (A more efficient check goes up to the square root, but this is simpler for beginners.)
            for i in range(2, (num // 2) + 1):
                if (num % i) == 0:
                    # If num is perfectly divisible by i, it's not prime
                    is_prime = False
                    break # No need to check further, we found a divisor

            # 4. Print the result based on our check
            if is_prime:
                print(f"{num} IS a prime number.")
            else:
                print(f"{num} is NOT a prime number.")

    except ValueError:
        # Handles cases where the user enters non-integer input
        print("Invalid input. Please enter a whole number or 'q' to quit.")
    except Exception as e:
        # Catches any other unexpected errors
        print(f"An unexpected error occurred: {e}")
    print("End of the Program")
