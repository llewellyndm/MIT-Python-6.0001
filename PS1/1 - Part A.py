# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 15:34:50 2020

@author: llewellyndm

This program calculates how many months it will take to save up enough money for a down
payment on a house, given your salary, how much you are prepared to save, and the cost of the house.
"""
annual_salary = float(input('How much do you earn each year?\n'))
portion_saved = float(input('How much, as a decimal, do you want to save each year?\n'))
total_cost = float(input('What is the cost of your dream home?\n'))
portion_down_payment = 0.25 #portion of house cost required for down payment
current_savings = 0 #starting off with no savings
r = 0.04 #annual interest earned on savings
month = 0

while current_savings < portion_down_payment*total_cost:
    current_savings = current_savings + (annual_salary/12)*portion_saved + current_savings*r/12
    month += 1

print('Number of months:', month)