# 2a
shopping_cost = float(input('What is the total price of your shopping?'))
discount_applicable = input('Do you have a discount code? y/n')

if (discount_applicable == 'y'):
    total_cost = shopping_cost * 0.9
# 2b
elif (shopping_cost >= 100):
	total_cost = shopping_cost * 0.95
else:
    total_cost = shopping_cost

# Extension
if (total_cost < 30):
	total_cost += 5
    
print(f'The total cost is {total_cost}')