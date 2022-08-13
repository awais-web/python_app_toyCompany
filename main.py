

'''Mr. Ahmad is satisfied with it. now he want to some modifications init
He also want to know total required budget for each order and profit.
the price of each item is mentioned below

main body: 40
side mirror: 8
Tyre: 12
Remote: 25

He sell 1 car in 500Rs
His other expenses at one car manufacturing is: 18Rs
'''

# to get order quantity
car = int(input("How many car order you received? : "))


# to calculate required number of parts with respect to order quantity
main_body = remote = car

tyres = 4 * car
side_mirrors = 2 * car


# output vaiable
required_items = f''' Mr. Ahmad you need 
Car Main Bodies: {main_body}; 
Side Mirrors: {side_mirrors};
Tyres: {tyres};
Remotes: {remote}
'''

# to calculate total costing and profit for this order
total_cost_1car = 40 +(2*8) + (4*12) + 25
other_expense = 18
profit = car * (500 - (18 + total_cost_1car))

print(required_items)

req_budget = car * total_cost_1car

print(f'Rquired Budget: {req_budget} for this order')

print(f'Total Profit: {profit} in this deal')

