print('Welcome to Bill Splitter')
bill = float(input('Enter the total bill amount: '))
people = int(input('How many people are splitting the bill?: '))
tip_perc = float(input('What percentage tip would you like to give?: '))
tip_amount = bill * (tip_perc/100)
print('Tip amount is', tip_perc)
bill_aft_tip = bill + tip_amount
per_person = bill_aft_tip / people
print('Your grand total is', bill_aft_tip)
print('Amount each person needs to pay is', per_person)