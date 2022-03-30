

def to_usd(my_price):
    """
    this is a docstring. it tells us what this function is about,
    what it's respobsibilities are, 
    what it's parameters are about, 
    what this function will return

    invoke like: to_usd(9.9999)
    """
    return '${:,.2f}'.format(my_price)

if __name__ == "__main__":
    
        
    #nesting code in main conditional will allow other scripts to cleanly import functions
    #this code still gets run when we invoke script from command line
    price = input("Please choose a price like 4.9999")

    print(to_usd(float(price)))

