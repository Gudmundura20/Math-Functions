# Þetta forrit skal hafa föll til stærðfræðilegra reikninga.
# Forritið skal útbúa valmynd sem prompta notanda fyrir þau föll sem forritið inniheldur
# Notandi skal geta valið föllin

def menu():
    '''Represent the functions in the program'''
    options = 'Please choose one of the options below: '
    a = 'a. Display the sum of the first N natural numbers.'
    b = 'b. Display the sum of the first N Fibonacci numbers.'
    c = 'c. Display the approximate value of e using N terms.'
    x = 'x. Exit from the program.'
    for option in (options, a, b, c, x):
        print(option)
        
def sum_natural(n_str):     
    '''Summa náttúrulegra talna í rununni (1, n)'''
    number = 1
    number_sum = 1
    while func_int >= 2:
        for number in range(1, func_int): # func_int er gefið frá notanda
            number += 1
            number_sum += number
        return number_sum  # return kemur út eftir því hvernig er kallað á fallið
    else:
        print('Error:', func_int, 'was not a valid number') # Þegar fallið er kallað
    
def sum_fibonacci(n_str):
    '''Fibonacci sequence sum'''
    first_n = 0
    second_n = 1
    fibo_sum = 1
    while func_int >= 2:
        for n in range(0, func_int-2): 
            step_value = first_n + second_n 
            first_n = second_n
            second_n = step_value # each value after gets the sum of the last two
            fibo_sum += step_value
        return fibo_sum
    else:
        print('Error:', func_int, 'was not a valid number')
    
#def approximate_euler(n_str):
    
menu() # Beginning of the program where the functions are represented
options = 'abc'
while True:
    n_str = input('Enter option: ')  # input 1
    
    if n_str == 'x':
        break # the whole program ends
    
    if n_str == 'a': # notandi vill sjá fall a.
        func_int = int(input('Enter N: ')) # input 2
        print('Natural number sum:',sum_natural('a'))
        continue
    elif n_str == 'b': # notandi vill sjá fall b.
        func_int = int(input('Enter N: ')) # input 2
        print('Fibonacci sum:',sum_fibonacci('b'))
    if not n_str in options:
        print("Unrecognized option", n_str)
        menu()                            # option was not a string that calls a function
    
    

    

    


    




    
