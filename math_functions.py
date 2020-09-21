# Þetta forrit skal hafa föll til stærðfræðilegra reikninga.
# Forritið skal útbúa valmynd sem prompta notanda fyrir þau föll sem forritið inniheldur
# Notandi skal geta valið föllin:
# sum_natural(n_str): , sum_fibonacci(n_str): , approximate_euler(n_str):
# og sett inn streng n_str(integer) sem gildi breytustærðar fallsins.
# Enter option: úttakið skal promptast eftir hvert fall sem er notað
# strengurinn x lokar forritinu, Enter option: x
# Úttakið "Unrecognized option k" þar sem k er invalid option fyrir þetta forrit
# 1. Valmynd falla 2a). input notanda, 2b) úttak um villuboð, 3. Túlka input notanda sem integer. Annars villuboð 4. Output.

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
        return number_sum
    else:
        return
    
#def sum_fibonacci(n_str)
    
#def approximate_euler(n_str):

#def exit():
    #return exit()
    
menu() # Beginning of the program where the functions are represented
options = 'abc'
while True:
    n_str = input('Enter option: ')  # input 1
    if not n_str in options:
        print("Unrecognized option", n_str)
        menu() # option was not a string that calls a function
        n_str = input('Enter option: ')
    if n_str == 'x':
        break # the whole program ends
    
    func_int = int(input('Enter N: ')) # input 2
    if n_str == 'a': # notandi vill sjá fall a.
        print('Natural number sum: ',sum_natural('a'))
        continue 
    

    

    


    




    
