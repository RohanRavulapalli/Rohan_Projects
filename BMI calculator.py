# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 10:44:56 2024

@author: rravu
"""

def BMI():
    '''
    This function calculates an individual's BMI based on their inputted height and weight.
    It also tells them whether they are in the healthy range for their ethnicity (as studies showcase
    certain ethnicities can be classified as overweight, on a population level, at an even lower BMI compared to 
    the traditonal caucasian BMI scale of 18.5 - 24.9)
    '''
    print('Please define whether you would like to enter your information using:')
    system = input('(a) Metric Units (CM, KG) \n(b) Imperial Units (Inches, Pounds) \npreference: ').strip()
    
    choices = ['a', 'b']
    
    while system.lower() not in choices:
        print('\nYou did not indicate which measurement system you would like to use. Please Try Again')
        system = input('(a) Metric System (CM, KG) \n(b) Imperial System (Inches, Pounds) \npreference: ')
        
    
    if system.lower() == 'a':
        height = float(input('\nPlease enter your height in Centimeters here: '))
        weight = float(input('\nPlease enter your weight in Kilograms here: '))
        
        BMI = BMI_Metric(height, weight)
        
    elif system.lower() == 'b':
        feet = float(input('\nPlease Enter Your Feet: '))
        inches = float(input('Please Enter Your Inches: '))
        height = feet*12 + inches
        weight = float(input('\nPlease enter your weight in Pounds here: '))
        
        BMI = BMI_Imperial(height, weight)
        
    BMI = round(BMI, 2)
    
    print('\nSome ethnic/racial groups have been shown to be classified as overweight, at a population level, at an even lower BMI ', end ="")
    print('compared to Caucasians when using the traditonal WHO defined scale. Therefore, In order to provide the best possible interpretation of your BMI, we require that you specify your ethnicity')
    print('\nPlease indicate which ethnic group best describes your origin')
    print('(a) African Carribean \n(b) Black African \n(c) Chinese \n(d) Japenese \n(e) Middle Eastern \n(f) South Asian \n(g) White European')
    Race = input('Answer: ').strip()
        
    
    Races = ['d', 'f', 'c', 'a', 'b', 'e','g']
    
    while Race not in Races:
        print('\nYou did not specify which ethnic/racial category best describes you. Please try again.')
        print('(a) African Carribean \n(b) Black African \n(c) Chinese \n(d) Japenese \n(e) Middle Eastern \n(f) South Asian \n(g) White European')
        Race = input('Answer: ').strip()
    
    if Race.lower() == 'g':
        verdict = White(BMI)
        
    else:
        verdict = Ethnic(BMI)
        
        
    print(f'\nYour BMI is: {BMI}')
    print(f'Based on your information, you are: {verdict}')
    
        
def BMI_Metric(height, weight):
    BMI = (weight/(height)/(height))*10000
    return BMI


def BMI_Imperial(height, weight):
    BMI = 703 * (weight/(height**2))
    return BMI
        
def White(Index):
    if Index >= 18.5 and Index <= 24.9:
        verdict = 'In the healthy weight range'
        
    if Index < 18.5:
        verdict = 'Underweight'
        
    if Index >= 25 and Index <= 29.9:
        verdict = 'Overweight'
        
    if Index >= 30:
        verdict = 'Obese'
    return verdict

def Ethnic(Index):
    if Index >= 18.5 and Index <= 22.9:
        verdict = 'In the healthy weight range'
        
    if Index < 18.5:
        verdict = 'Underweight'
        
    if Index >= 23 and Index <= 27.5:
        verdict = 'Overweight'
        
    if Index > 27.5:
        verdict = 'Obese'
    return verdict
    
def Main():
    BMI()
Main()
    

