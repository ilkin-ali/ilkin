elements = {'hydrogen':
                {'number': 1,
                 'weight': 1.00794,
                 'symbol': 'H',
                 'is_noble_gas':0},
            'helium':
                {'number': 2,
                 'weight': 4.002602,
                 'symbol': 'He',
                 'is_noble_gas':1}}

helium = elements["helium"]  # get the helium dictionary
print(helium)
hydrogen_weight = elements["hydrogen"]["weight"]  # get hydrogen's weight
print(hydrogen_weight)
#
print("\n")
#

oxygen = {"number":8,"weight":15.999,"symbol":"O"}  # create a new oxygen dictionary
elements["oxygen"] = oxygen  # assign 'oxygen' as a key to the elements dictionary
print('elements = ', elements)
#
print("\n")
#

print(bool(elements['hydrogen']['is_noble_gas'])) # bool for making parantheses boolean
print(bool(elements['helium']['is_noble_gas']))