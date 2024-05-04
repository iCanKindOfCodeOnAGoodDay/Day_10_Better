"""

    Scott Quashen
    London App Brewery
    100 Days of Python Code: Day 10-B
    May 03 2024

    ------
    Description:    Console Calculator - Improved Program
    ------
    
    ------
    Inputs:         Console input (math commands, numbers) 
    ------
    
    ------
    Outputs:        Console output (results)
    ------
    
    ------
    Dependencies:   os. # used to clear the console incrementally 
    ------

    ------
    Assumptions:    Developed and tested using Spyder 5.15.7, Python version 3.11.5 on macOS 14.4.1
    ------
    
"""

import os # used to clear the console

# declare the constant globally
console_art = """ 
              .__                              
  ____ _____  |  |   ____                      
_/ ___\\__  \ |  | _/ ___\                     
\  \___ / __ \|  |_\  \___                     
 \___  >____  /____/\___  >                    
     \/     \/          \/                     
                      .__    .__               
  _____ _____    ____ |  |__ |__| ____   ____  
 /     \\__  \ _/ ___\|  |  \|  |/    \_/ __ \ 
|  Y Y  \/ __ \\  \___|   Y  \  |   |  \  ___/ 
|__|_|  (____  /\___  >___|  /__|___|  /\___  >
      \/     \/     \/     \/        \/     \/ 

""" 

def main():
    
    """
    
    Description -   Runs calc on a loop. Allows follow up calculations
    ----------
    Input -         User input, nums, math command, request for exit or continue
    ----------
    Output -        Calculator, results, text to console, etc.
    -------

    """ 
    
    while True: # when exit, restart the calculator, runs program in a loop
    
        keep_going = True
        
        num1 = 0
        
        should_override_num1 = False
        
        while keep_going == True: # continue calculating with previous result set to first number
        
            os.system('clear')
            
            operations = {'+': add, '-': subtract, '*': multiply, '/': divide }
            
            print(console_art)
            
            if should_override_num1 == False:

                num1 = try_convert_input_integer('Type the first number: ')
                
            selected_operation = request_symbols( operations )
                        
            os.system('clear')
                
            print(f'{num1} {selected_operation} ')
            
            num2 = try_convert_input_integer('Type the second number: ')
            
            os.system('clear')
            
            print('')
            
            function = operations[selected_operation] # choose the name of the function from our dictionary
            
            r = function(num1, num2) # call one of the mathg functions by name above
            
            print(console_art)
        
            print(f'{num1} {selected_operation} {num2} = {r}')
            
            typed_yes_or_no = False
            
            while typed_yes_or_no == False: # if yes, we override the num1 to the result to continue calculating on that 
                
                request_exit = input('Type continue or exit: ')
                
                if request_exit == 'exit':
                    keep_going = False
                    typed_yes_or_no = True
                    
                elif request_exit == 'continue':
                    num1 = r
                    should_override_num1 = True
                    typed_yes_or_no = True

def try_convert_input_integer( prompt ):
    
    """
    
    Description -   Modified input func that takes only an int
    ----------
    Input -         Pass in input prompt
    ----------
    Output -        Returns int, or prints error and asks the user again
    -------

    """ 
    
    should_try_again = True
    
    while should_try_again == True:
        
        try: 
            num = float(input(prompt))
            
            return num        
        except:
            print('Whoops. Please type an integer.')
            
    
# add any number return Float or int
def add(n1, n2):
    return n1 + n2

# subtract any number return Float or int
def subtract(n1, n2):
    return n1 - n2

# multiply any number return Float or int
def multiply(n1, n2):
    return n1 * n2

# divide any number return Float or int
def divide(n1, n2):
    return n1 / n2

def request_symbols( operations_dict ):
    
    """
    
    Description -   Modified input func only accepts correct symbols
    ----------
    Input -         Pass the dictionary of symbols (prints them too)
    ----------
    Output -        Returns symbol, or prints error and asks the user again
    -------

    """ 
    
    while True:

        for o in operations_dict:
            print(o)
            
        selected_operation = input('Type a symbol: ')
        for o in operations_dict:
            if selected_operation == o:
                return selected_operation
            
        os.system('clear')

        print('please try again')
        
# run
if __name__ == '__main__':
    main()
