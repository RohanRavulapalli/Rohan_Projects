# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 23:19:24 2024

@author: rravu
"""


def equation():
    equation = input('Please enter your quadratic function here: ')
    
    while '^2' not in equation:
        print('\nThe equation you entered is not quadratic.')
        print(' ')
        equation = input('Please enter your quadratic function here: ')
    
    equation = equation.replace(' ', '').replace('+', '').lower()
    
    for char in equation:
        if char.isalpha():
            equation = equation.replace(char, 'x')
            
            
    charlist = list(equation)
    
    coefficients = []
    
    if equation.count('x') == 2:
        
        for char in charlist:
            index = charlist.index(char)
            if char == '^':
                charlist.pop(index)
                charlist.pop(index)
    
        for char in charlist:
            if char.isalpha():
                i = charlist.index(char)
                coeff = charlist[0:i]
                coefficients.append(''.join(coeff))
                charlist = [m for m in charlist[i+1:]]
        
        if charlist: # Checks if charlist is empty
            final_coeff = ''.join(str(m) for m in charlist)
        
        else:
            final_coeff = 0 
        
        coefficients.append(final_coeff)
        
        for i in range(len(coefficients)-1):
            if coefficients[i] == '':
                coefficients[i] = 1
            if coefficients[i] == '-':
                coefficients[i] = -1
    else:
        
         for i in range(len(charlist)):
             if charlist[i] == 'x':
                coefficients.append(''.join(charlist[:i]))
             if charlist[i] == '^':
                coefficients.append(''.join(charlist[i+2:]))
                 
         coefficients.insert(1, 0)
         
         if coefficients[0] == '':
             coefficients[0] = 1
              
         if coefficients[0] == '-':
             coefficients[0] = -1 
             
         if coefficients[2] == '':
             coefficients[2] = 0
             
    coefficients = [int(num) for num in coefficients]
    
    print(f'\ncoefficients: a = {coefficients[0]}, b = {coefficients[1]}, c = {coefficients[2]}')
     
    return coefficients

def Formula(equation_): # Accessing global variable equation_
    import cmath
    import math
    a = equation_[0]
    b = equation_[1]
    c = equation_[2]    
    radicand = ((b)**2) - (4*a*c)
    denominator = 2*a 
    if radicand >= 0:
        numerator_addition = -1*b + math.sqrt(radicand)
        numerator_subtraction = -1*b - math.sqrt(radicand)
    else:
        numerator_addition = -1*b + cmath.sqrt(radicand)
        numerator_subtraction = -1*b - cmath.sqrt(radicand)
    answer = numerator_addition/denominator, numerator_subtraction/denominator
    return answer

def main():
    equation_ = equation() # Note: when defining global variables under the main() functions as opposed to just defining them outside, you must define the variable
    # name as different than the function name. If you set equation = equation(), this leads to confusion for python since equation itself is defined as a function.
    
    answer = Formula(equation_)
    print(' ')
    print('answer:', f'x = {answer[0]}, x = {answer[1]}')
    

if __name__ == "__main__":
    main()