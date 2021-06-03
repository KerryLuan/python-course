#1a
#shirt_price = float(input('What is the price of the shirt?'))
#shirt_in_budget = shirt_price <= 25.00
#print(f'Shirt is available within budget: {shirt_in_budget}')

#1b
shirt_price = float(input('What is the price of the shirt?'))
shirt_colour = input('What colour is the shirt?')

shirt_in_budget_and_colour = shirt_price <= 25.00 and shirt_colour.lower() == 'yellow'

print(f'Shirt is available within budget and correct colour: {shirt_in_budget_and_colour}')