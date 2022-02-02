# Convert a signed float of dollars to an absolute value in cents
# Author: Jamie Roche

dollars = float(input("Please enter an amount: "))
cent = round(dollars * 100)
absoluteValue = abs(cent)
print('That amount in cent is: {}'.format (absoluteValue))