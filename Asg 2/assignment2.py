'''
Assignment 2
Noah Pouliot
Student ID: 261282564
By submitting this file, I declare that I did the assignment on
my own according to the rules specified in the assignment PDF
'''
import doctest
#Question 1 - Binary manipulation
def count_set_bits(num:int):
    '''
    This function counts the number of set bits (1s) in the binary representation of a given integer.
    It converts an integer to binary, and counts the number of 1s.
    Ex:
    >>> print(count_set_bits(13))
    3
    >>> print(count_set_bits(5))
    2
    >>> print(count_set_bits(0))
    0
    >>> print(count_set_bits(255))
    8
    >>> print(count_set_bits(16))
    1
    '''
    
    # Convert the integer to its binary representation 
    binary_representation = ''
    while num > 0:
        binary_representation = str(num % 2) + binary_representation
        num = num // 2
    
    #Count the number of '1's
    count = binary_representation.count('1')
    
    return count

def is_power_of_two(num:int):
    '''
    This function checks if a given integer is a power of two.
    It returns True if the number is a power of two, and False otherwise.
    Ex:
    >>> print(is_power_of_two(1))
    True
    >>> print(is_power_of_two(2))
    True
    >>> print( is_power_of_two(3))
    False
    >>> print( is_power_of_two(4))
    True
    >>> print( is_power_of_two(5))
    False
    >>> print( is_power_of_two(16))
    True
    '''
    # A number is a power of two if it has exactly one set bit in its binary representation
    if count_set_bits(num) == 1:
        return True
    return False

def approximate_binary(x:float, epsilon:float, max_frac_bits:int):
    '''
    This function approximates a non-negative decimal float x as a fixed-point binary string, namely the integer and fractional parts separated by a binary point. 
    The approximation should either satisfy |approx - x| <= epsilon, or a maximum number of bits is reached.
    Ex:
    >>> print(approximate_binary(3.25, 1e-6, 256))
    ('11.01', 3.25)
    >>> print(approximate_binary(0.1, 1e-6, 40))
    ('0.00011001100110011001', 0.09999942779541016)
    >>> print(approximate_binary(0.1, 1e-6, 10))
    ('0.0001100110', 0.099609375)
    >>> print(approximate_binary(8.0, 1e-6, 256))
    ('1000.', 8.0)
    '''
    if x < 0 or epsilon <= 0 or (max_frac_bits < 0 or max_frac_bits > 256):
        raise ValueError("Invalid input values. Ensure x is non-negative, epsilon is positive, and max_frac_bits is non-negative, up to 256.")
    x_integer = int(x)
    x_fraction = x - x_integer
    
    # Convert the integer part to binary
    if x_integer == 0:
        binary_integer = '0'
    else:
        binary_integer = ''
        while x_integer > 0:
            binary_integer = str(x_integer % 2) + binary_integer
            x_integer = x_integer // 2
    
    # Convert the fractional part to binary
    binary_fraction = ''
    approx_value = int(binary_integer, 2)
    for i in range(max_frac_bits):
        x_fraction *= 2
        bit = int(x_fraction)
        binary_fraction += str(bit)
        x_fraction -= bit
        
        # Check if the approximation is within the desired epsilon (before max frac bits is reached)
        approx_value += bit * (2 ** -(len(binary_fraction)))
        if abs(approx_value - x) <= epsilon:
            break
    
    #Combine both parts
    binary_string = ''
    if binary_fraction.count('1') == 0:
        binary_string = binary_integer+'.'
    else:
        binary_string = binary_integer + '.' + binary_fraction
    return binary_string, approx_value

#Question 2 - Triangular Numbers and Seating
def is_triangular(num:int):
    '''
    This function checks if a given integer is a triangular number.
    It returns True if the number is triangular, and False otherwise.
    Ex:
    >>> print(is_triangular(1))
    True
    >>> print(is_triangular(3))
    True
    >>> print(is_triangular(5))
    False
    >>> print(is_triangular(15))
    True
    >>> print(is_triangular(20))
    False
    '''
    n = 0
    triangular_number = 0
    while triangular_number < num:
        n += 1
        triangular_number = n * (n + 1) // 2
    return triangular_number == num

def num_rows_in_triangle(n:int):
    '''
    This function calculates the number of rows in a triangular arrangement given n seats.
    It returns the number of complete rows that can be formed with n people.
    Ex:
    >>> print(num_rows_in_triangle(1))
    1
    >>> print(num_rows_in_triangle(10))
    4
    >>> print(num_rows_in_triangle(13))
    4
    '''
    N = 0
    T_N = 0
    while T_N <= n:
        N += 1
        T_N = N * (N + 1) // 2
    
    return N - 1

def arrange_guests(G:int):
    '''
    This function arranges G guests into a triangular seating arrangement.
    It returns the number of rows, number seated in full triangle and the number of leftover guests.
    >>> arrange_guests(8)
    (3, 6, 2)
    >>> arrange_guests(15)
    (5, 15, 0)
    '''
    if G < 0:
        raise ValueError("Number of guests must be non-negative.")
    
    N= num_rows_in_triangle(G)
    T_N = N * (N + 1) // 2
    L =  G-T_N
    
    return N, T_N, L

def make_triangle_string(G:int, max_seats_per_row:int):
    '''
    This function creates a string representation of the triangular seating arrangement for G guests, in rows of a max num of seats.
    It returns a string where '*' represents a guest and '-' represents an empty seat.
    Ex:
    >>> print( make_triangle_string(18, 22) ) 
    ----*----------------o
    ---*-*---------------o
    --*-*-*--------------o
    -*-*-*-*--------------
    *-*-*-*-*-------------
    >>> print( make_triangle_string(15, 12))
    ----*-------
    ---*-*------
    --*-*-*-----
    -*-*-*-*----
    *-*-*-*-*---
    >>> print( make_triangle_string(18, 5) )
    ERROR, not enough seats
    '''
    N, T_N, L = arrange_guests(G)
    triangle_string = ''
    min_seats_last_row = 2*N - 1
    if max_seats_per_row < min_seats_last_row or (L == N and max_seats_per_row == min_seats_last_row):
        return ("ERROR, not enough seats")
    for row in range(1, N + 1):
        row_string = (N-row)*'-' + '*-'*(row-1) + '*'+ (N-row)*'-' + (max_seats_per_row - (2*N - 1)) * '-'
        if row <= L:
            row_string = row_string[:-1] + 'o'
        triangle_string += row_string 
        if row != N:
            triangle_string += '\n'
    return triangle_string
    
doctest.testmod()