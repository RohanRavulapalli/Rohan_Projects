# -*- coding: utf-8 -*-
"""
Goblins Magical Loan System
A sophisticated system for approving loans to wizards starting businesses.

"I have neither given nor received help on this assignment."
author: Rohan Ravulapalli
"""
__version__ = 4

#(1) main: Calls the other functions and controls data flow
def main():
    '''
    Main function that calls all the other functions and provides
    an interactive loan processing experience.
        
    Args:
        None
    Returns:
        None
    '''
    print_introduction()
    name = input_name()
    rating = calculate_rating(name)
    print_rating(rating)
    loan_amount = input_loan_amount()
    print_loan_availability(rating, loan_amount)
    test_loan(rating, loan_amount)
    print_conclusion()

#(2) print_introduction: Print a welcome message
def print_introduction():
    '''
    function prints a greeting message to the user.
    
    args:
        none
    returns:
        none
    '''
    print('''* 1) Introduction ********************************
Welcome to the Goblins Magical Loan System!
Please answer the following questions truthfully,
and we will process your loan request.
Imposters will be fed to the dragons.''')
    
#(3) input_name: Get the user's name
def input_name() -> str:
    '''
    functions prompts user to enter their name for identity
    verification.
    
    args:
        none
    returns:
        a string value of the user's name after inputted.
    '''
    name = input('''* 2) Name ****************************************
Please enter your full, legal name.
Magical verification will verify your identity.
Write your name and press enter: ''')
    print("Welcome,", name + "!")
    return name

#(4) calculate_rating: Get the user's rating (by Grindlehook)
# The following is Grindlehook's function. Do not modify it.
# You should not worry about HOW it works, but instead think of its
# arguments and return value. Remember you can only call it once!
# Do NOT change the following function definition
def calculate_rating(name):
    '''
    Returns the customer's credit rating, according to the bank's current
    status, the customer, and the alignment of the stars. This function
    is a little delicate, and will break after being called once.
    
    NOTE (ghook@1/15/2018): DO NOT TOUCH THIS, I FINALLY GOT IT WORKING.
    
    Returns:
        int: An integer (0-9) representing the customer's credit rating.
    '''
    c=calculate_rating;setattr(c,'r',lambda:setattr(c,'o',True))
    j={};y=j['CELESTIAL_NAVIGATION_CONSTANT']=10
    j[True]='CELESTIAL_NAVIGATION_CONSTANT'
    x=str(''[:].swapcase);y=y+11,y+9,y+-2,y+-2,y+4,y+-5,y+-1,y+11,y+9,\
    y+-6,y+-6,y+-1,y+-5,y+3,y+-7,y+7,y+-1,y+-5,y+8,y+-7,y+11,y+1
    z=lambda x,t,o=0:''.join(map(lambda j:x.__getitem__(j+o), t))
    if hasattr(c,'o')and not getattr(c, 'o'): return z(x,y)
    c.o=False;j['CELESTIAL_NAVIGATION_CONSTANT'].bit_length
    d=(lambda:(lambda:None))()();g=globals()
    while d:g['X567S-lumos-17-KLAUS']=((d)if(lambda:None)else(j))
    p=lambda p:sum(map(int, list(str(p))))
    MGC=p(sum(map(lambda v: v[0]*8+ord(v[1]), enumerate(name))))
    while MGC>10:MGC=p(MGC)
    if c:return MGC
    
# Do NOT change the preceding function definition
    
#(5) print_rating: Print the user's rating
def print_rating(rating):
    '''
    function prints the user's rating calculated from
    the calculate_rating function.
    the rating variable was assigned to the calculate_rating function
    in the main() function.
    
    args:
        rating(int): integer value representing user's rating.
        Is computed from calculate_rating function
        
    returns:
        none
    '''
    print('''* 3) Rating **************************************
Your user rating has been calculated.
Your rating is:''',str(rating)+"/10","points")

#(6) input_loan_amount: Get the user's desired loan amount
def input_loan_amount()->int:
    '''
    function prompts user to enter their desired
    loan amount, and then returns the amount as
    an integer value. The loan_amount function was
    assigned to this function under the main()
    function definition.
    
    args:
        none
    returns:
        int value representing user's desired loan amount
    '''
    print('''* 4) Loan ****************************************
Loans are made based on your customer rating.
However, you can request a loan of any size.
How many galleons do you want?''')
    return int(input("Write your loan amount: "))
    
#(7) print_loan_availability: Print whether the loan is available
def print_loan_availability(rating, loan_amount):
    '''
    function prints whether the user's requested loan is
    available or not by printing the returned value of
    the test_loan function, which gives a boolean value.
    
    args:
        rating(int): integer value representing user's rating.
        Is computed from calculate_rating function
        
        loan_amount(int): integer value representing user's
        desired loan amount. Is computed from the
        input_loan_amount function.
    returns:
        none.
    '''
    print('''* 5) Available? **********************************
Your loan request has been evaluated.\nLoan available:''', test_loan(rating, loan_amount))
    

#(8) test_loan: Determines if the loan is available
def test_loan(rating, loan_amount)->bool:
    '''
    function tells user whether their loan request,
    based on their rating and desired loan amount, is
    available.
    
    args:
        rating(int): integer value representing user's rating.
        Is computed from calculate_rating function
        
        loan_amount(int): integer value representing user's
        desired loan amount. Is computed from the
        input_loan_amount function.
    returns:
        boolean value representing whether the loan
        is available or not (True if available,
        False if not available)
    '''
    return (rating**2)*100 >= loan_amount

#(9) print_conclusion: Prints a thank-you message.
def print_conclusion():
    '''
    Function prints thank you message to user
    after using the GMLS system.
    
    args:
        none
    returns:
        none
    '''
    print('''* 6) Conclusion **********************************
Thanks for using Goblins Magical Loan System!
Best of luck with your new small business.
We hope you'll use Goblins for all your future
banking needs. Remember: Fortius Quo Fidelius!
**************************************************''')
# Call main function only if this file is being run directly
#   as opposed to being run by `test_my_solution.py`
       
