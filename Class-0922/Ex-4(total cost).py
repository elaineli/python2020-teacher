# Total cost

# A cupcake costs 1 dollars and 98 cents.
# Determine, how many dollars and cents should one pay for 10 cupcakes.
# It should print "total cost of 10 cupcakes is 19 dollars and 80 cents"

numCupcakes = 10

totalCostDollar = numCupcakes * 1 + (numCupcakes * 98) // 100
totalCostCents = (numCupcakes * 98) % 100

print('total cost of 10 cupcakes is', totalCostDollar, 'and', totalCostCents, 'cents')

# Test if there are 20 cupcakes

