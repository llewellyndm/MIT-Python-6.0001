# =============================================================================
# This program allows the user to find the best savings rate that allows them
# to save enough money for a down payment on a house costing 1,000,000 in 3 
# years (within $100). It does so by using bisection search.
# =============================================================================
starting_salary = float(input('How much do you earn each year? '))
total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = 0.25
current_savings = 0
r = 0.04 #annual interest rate on savings
month = 0
high = 1
low = 0
steps = 0
enough = True #this determines whether the user's salary is high enough for a down payment
portion_saved = 1
# start with a savings rate of 1 because if this rate is not high enough the 
# program can conclude that the user is unable to save enough with their salary

while abs(current_savings - portion_down_payment*total_cost) > 100:
    current_savings = 0 # reset savings
    annual_salary = starting_salary
    # for each new savings rate tested, this resets the salary to its 
    # initial value at the start of the three years.
    for month in range(1,37): 
        current_savings = (current_savings + (annual_salary/12)*portion_saved 
                           + current_savings*r/12)
        if month%6 == 0:
            annual_salary = annual_salary + annual_salary*semi_annual_raise
    steps += 1
    # now we update the endpoints of the domain in which we are performing bisection search.
    if current_savings > portion_down_payment*total_cost:
        high = portion_saved
    elif current_savings < portion_down_payment*total_cost:
        low = portion_saved
        if low == 1:
            print('It is not possible to pay the down payment in 3 years.')
            enough = False
            break
    portion_saved = (high + low)/2 #new value from bisection search
    
if enough: #ignored if salary is too low
    print('Best savings rate:', portion_saved)
    print(steps, 'steps')
