# Suppose the cover price of a book is $24.95, but bookstores get a 40% discount.
# Shipping costs $3 for the first copy and 75 cents for each additional copy.
# What is the total wholesale cost for 60 copies?

numBooks = 60

totalBookCost = numBooks * (1 - 0.4) * 24.95

totalShippingCost = 3 + 0.75 * (numBooks - 1)

print('The total whole cost for 60 copies is $', totalBookCost + totalShippingCost)