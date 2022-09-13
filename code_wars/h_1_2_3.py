"""Messi is a soccer player with goals in three leagues:

LaLiga
Copa del Rey
Champions
Complete the function to return his total number of goals in all three leagues.

Note: the input will always be valid.
"""
def sum_total_fusbol(la_liga,copa,Champions):
    x = la_liga + copa + Champions
    print(x)
sum_total_fusbol(10,5,2)
sum_total_fusbol(10,2,2)



"""Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.
For example: month 2 (February), 
is part of the first quarter; month 6 (June), is part of the second quarter; 
and month 11 (November), is part of the fourth quarter."""


def quarter_of(month):
    q = {1: (1,3), 2:(4,6), 3:(7,9), 4:(10,12)}
    print( [k for k,v in q.items() if v[0] <= month <= v[1]][0])
quarter_of(10)

"""This function should test if the factor is a factor of base.

Return true if it is a factor or false if it is not.

About factors
Factors are numbers you can multiply together to get another number.

2 and 3 are factors of 6 because: 2 * 3 = 6

You can find a factor by dividing numbers. If the remainder is 0 then the number is a factor.
You can use the mod operator (%) in most languages to check for a remainder
For example 2 is not a factor of 7 because: 7 % 2 = 1

Note: base is a non-negative number, factor is a positive number.

"""

def check_for_factor(base, factor):
    return base % factor == 0