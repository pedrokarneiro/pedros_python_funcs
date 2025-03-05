def rnd_3_dgt() -> int:
    '''
    This function generates a random
    three-digit number.
    '''
    # Importing the function (randint)
    # from the module (random)
    from random import randint

    # randint generates a random
    # number in the given range
    n = randint(100, 999)

    return n

def first_o_3_dgts(num: int) -> int:
    # The first digit (the most significant)
    # of the number is extracted
    # by dividing it by 100.
    c = n // 100
    return c

def second_o_3_dgts(num: int) -> int:
	# The last digit of the number
    # is deleted by dividing by 10 whole.
    # Then finding the remainder when
    # dividing by 10 extracts the last digit,
    # which in the original number
    # was in the middle.
    d = (n // 10) % 10
    return d

def third_o_3_dgts(num: int) -> int:
    # The last digit (the lowest digit)
    # of the number is extracted
    # by finding the remainder
    # by division by 10.
    u = n % 10
    return u

def sum_o_3_dgts(num: int) -> int:
    '''
    This function calculates the sum
    of the digits of a three-digit number.
    '''
    c = first_o_3_dgts(num)
    d = second_o_3_dgts(num)
    u = third_o_3_dgts(num)
    # The sum of digits is calculated.
    return c+d+u

def sum_o_dgts_o_rnd_3_dgt() -> int:
    '''
    This function generates a random
    three-digit number and calculates
    the sum of its digits.
    '''
    n = rnd_3_dgt()
    n = sum_o_3_dgts(n)
    # The sum of digits is displayed.
    print(n)

# EXPECTED RESULTS:
# =================
# Input number: 801
# Output number: 9

