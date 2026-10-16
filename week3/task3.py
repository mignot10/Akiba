def is_prime(number):
    """Determine whether a number is prime. Numbers <= 1 are not prime."""
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def get_divisors(number):
    """Return all positive divisors of a number."""
    if number == 0:
        return "Undefined (0 has infinite divisors)"
    
    num = abs(number)
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def sum_of_digits(number):
    """Return the sum of its digits (ignoring the negative sign)."""
    num = abs(number)
    return sum(int(digit) for digit in str(num))

def reverse_number(number):
    """Return the reversed number, preserving the negative sign if applicable."""
    if number < 0:
        return -int(str(abs(number))[::-1])
    return int(str(number)[::-1])

def analyze_number(number):
    """Return a complete analysis dictionary for the given number."""
    # Handle even/odd parity correctly for negative numbers and zero
    is_even = number % 2 == 0
    parity = "Even" if is_even else "Odd"
    
    analysis = {
        "number": number,
        "parity": parity,
        "is_prime": is_prime(number),
        "sum_of_digits": sum_of_digits(number),
        "reversed_number": reverse_number(number),
        "divisors": get_divisors(number)
    }
    return analysis

def print_analysis(number):
    """Helper function to cleanly display the analysis report."""
    result = analyze_number(number)
    print(f"\n--- Analysis for: {result['number']} ---")
    print(f"Parity          : {result['parity']}")
    print(f"Is Prime?       : {result['is_prime']}")
    print(f"Sum of Digits   : {result['sum_of_digits']}")
    print(f"Reversed Value  : {result['reversed_number']}")
    print(f"Divisors        : {result['divisors']}")

if __name__ == "__main__":
    # Test cases including standard, zero, and negative numbers
    test_numbers = [123, 0, -45, 7]
    
    for num in test_numbers:
        print_analysis(num)