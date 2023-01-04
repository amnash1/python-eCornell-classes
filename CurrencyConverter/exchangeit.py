"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and amount.
It prints out the result of converting the first currency to the second.

Author: Andy Nash
Date:   2022-10-26
"""
import currency

src = input('3-letter code for original currency: ')
src = str(src)

dst = input('3-letter code for the new currency: ')
dst = str(dst)

amt = input('Amount of the original currency: ')
amt = str(amt)

result = round(currency.exchange(src,dst,amt),3)
result = str(result)

print('You can exchange '+amt+' '+src+' for '+result+' '+dst+'.')
