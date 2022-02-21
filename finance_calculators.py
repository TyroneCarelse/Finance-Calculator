import math

#Program shows calculator for investment or bond, depending on user input.

earn = "investment"
pay = "bond"

#input requested from user

finType = input("Choose either investment or bond from the menu below to proceed: ").lower()

if finType == "investment":
    
    print("You selected" + " " + earn)
    
    p = float(input("Enter the principal amount: "))
    t = float(input("Enter the duration in years: "))
    r = float(input("Enter the annual interest rate: "))
    
    interest = input("simple or compound interest? ").lower()

# function for simple and compound interest

    simple_interest = p*(1+(r/100)*t) 
    comp_amt = p*math.pow((1+(r/100)),t)

# input requested from user for type of interest to be calculated

    if interest == "simple":
        print("Total Amount with simple interest = R% .2f" %simple_interest)
    
    elif interest == "compound":
        print("Total Amount with compound interest = R% .2f" %comp_amt)

else:
    
    print("You selected" + " " + pay)

    p = float(input("Enter the present value of the house: "))
    interest_rate = float(input("Enter the interest rate: "))
    duration = float(input("Enter the number of months over which your bond will be paid: "))

    i = interest_rate/(100*12) # convert from annual to monthly rate
    n = duration*12  # convert from total years to months

#function for calculating bond repayments
  
    bond_repay =  p*((i*((i+1)**n))/(((i+1)**n)-1))

#calculating the output
    
    finType == "bond"
    print("Total monthly payment is = R% .2f" %bond_repay)
