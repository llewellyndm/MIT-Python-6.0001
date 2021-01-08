# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 18:20:56 2020

@author: llewellyndm

This program calculates how many months it will take to save up enough money for a down
payment on a house, given your salary, how much you are prepared to save, and the cost of the house.
It also takes into  account a semi-annual raise, specified by the user.
"""

annual_salary = float(input('How much do you earn each year?\n'))
portion_saved = float(input('How much, as a decimal, do you want to save each year?\n'))
total_cost = float(input('What is the cost of your dream home?\n'))
semi_annual_raise = float(input(('As a decimal, how much does your salary rise every 6 months?\n')))
portion_down_payment = 0.25 #portion of house cost required for down payment
current_savings = 0
r = 0.04 #annual interest rate on savings
month = 0

while current_savings < portion_down_payment*total_cost:
    month += 1    
    current_savings = current_savings + (annual_salary/12)*portion_saved + current_savings*r/12
    #if necessary, the salary must be changed after current_savings is calculated
    if month%6 == 0: #if the current month is the 6n-th month, where n is integer
        annual_salary = annual_salary + annual_salary*semi_annual_raise #change salary according to raise

print('Number of months:', month)