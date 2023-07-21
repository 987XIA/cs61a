def split(n):
    """split positive n into all but its last digits and its last digit."""
    return n // 10, n % 10

def sum_digits(n):
    """Return the sum of the digits of positive number n.
    """
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last

def sum_digits_iter(n):
    """iteration version of sum digits"""
    digits_sum = 0
    while n > 0:
        n, last = split(n)
        digits_sum += last
    return digits_sum



"""luhn algotithm is for checking whether the credit card number is valid
    using double recurcive
"""

def luhn_sum(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last

def luhn_sum_double(n):
    all_but_last, last = split(n)
    luhn_digits = sum_digits(2 * last)
    if n < 10:
        return luhn_digits
    else:
        return luhn_sum(all_but_last) + luhn_digits